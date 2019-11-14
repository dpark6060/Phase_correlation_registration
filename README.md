# Phase Correlation Registration
Performs translational registration to T1 images

Frequency domain manipulation is superior to spatial transformations for preserving voxel-level detail.  Spatial transformations apply interpolation to the voxels, destroying the original data and resulting in unavoidable blurring.

frequency domain transformations preserve the full original information, and only apply a known, quantafiable phase shift to the image.  If desired, the original data can be recovered completely by applying an inverse phase correction.  No blurring is introduced with this method.

wrkdir is an input directory that contains ONLY the t1 images you wish to work on.  


Uses test data from https://www.dropbox.com/sh/myfy8hdfdldn99v/AAChKo-hOZRQALEvpc33hJAUa/FNK_001_2019-10-23?dl=0&subfolder_nav_tracking=1

Supporting literature:

https://www.researchgate.net/profile/Carl-Fredrik_Westin/publication/224744658_Registration_of_multidimensional_image_data_via_subpixel_resolution_phase_correlation/links/0912f512b8f28e9694000000/Registration-of-multidimensional-image-data-via-subpixel-resolution-phase-correlation.pdf

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.543.9776&rep=rep1&type=pdf

https://en.wikipedia.org/wiki/Phase_correlation

https://www.semanticscholar.org/paper/Phase-Correlation-Based-Image-Alignment-with-Alba-Aguilar-Ponce/a631d423cae1cacbb08eb63a8f04fdc197b53ec7
