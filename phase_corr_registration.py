#!/usr/bin/env python3

import numpy as np
import nibabel as nb
import matplotlib.pyplot as pl
import sys
import os
import glob
import shutil



def calc_shift3D(ref, img, mult = 1):

    x,y,z = np.shape(ref)

    # Upsampling for higher resolution if desired, but it doesn't really work at the moment so don't use it
    x *= mult
    y *= mult
    z *= mult

    mx = int(x/2)
    my = int(y/2)
    mz = int(z/2)

    # Take the 3d fft
    f_ref = np.fft.fftn(ref, (x,y,z), axes=(0,1,2))
    f_img = np.fft.fftn(img, (x,y,z), axes=(0,1,2))

    # use the normnalized phase correlation equation
    f_q = np.divide(np.multiply(f_ref, np.conj(f_img)), np.multiply(np.abs(f_ref), np.abs(np.conj(f_img))))
    q = np.fft.fftn(f_q, (x,y,z), axes=(0,1,2))

    # This also doesn't work...I'm trying to identify the i/j/k shift values (in pixels), but for some reason it doesn't
    # work.  I think things are a little too noisy maybe?

    maxn = np.argmax(np.abs(q))
    i, j, k = np.unravel_index(maxn, (x, y, z))
    print('shift: {} {} {}'.format(i,j,k))

    return f_img, f_q


def apply_shift_3d(f_img, f_shift,shape):

    f_out = np.multiply(f_img,f_shift)

    out = np.fft.ifftn(f_out, axes=(0,1,2))
    return out




def main2(wrkdir,ref=''):

    files = glob.glob(os.path.join(wrkdir, '*MPRAGE_Ti*.nii.gz'))
    output_dir = os.path.join(wrkdir, 'processed')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    if len(files) == 0:
        print('No files')
        sys.exit(1)

    if not ref:
        ref=files[0]

    nfile = 0
    ref_base = os.path.split(ref)[-1]
    output_name = os.path.join(output_dir, ref_base)
    shutil.copy(ref, output_name)
    ref_nii = nb.load(ref)
    ref_data = ref_nii.get_data()

    len_files = len(files)
    print('{} files found'.format(len_files))
    print('ref: {}'.format(ref))

    for f in files:
        print('file {} of {}'.format(nfile,len_files))
        if f == ref:
            continue
        nfile += 1

        nii = nb.load(f)
        data = nii.get_data()

        # Calculate the shift
        f_img, f_q = calc_shift3D(ref_data, data, 1)

        # Apply the shift
        shifted2 = apply_shift_3d(f_img, f_q, data.shape)
        shifted2 = np.abs(shifted2)

        # Save the file
        fbase = os.path.split(f)[-1]
        output_name = os.path.join(output_dir,fbase)
        niout = nb.Nifti1Image(shifted2, ref_nii.affine, ref_nii.header)
        nb.loadsave.save(niout,output_name)



if __name__ == '__main__':

    wrkdir = '/Users/davidparker/Documents/MyWork/FFT_reg/EXVIVO/FNK_001_2019-10-23/'
    main2(wrkdir)
















