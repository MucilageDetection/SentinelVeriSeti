# Bahri ABACI
# Save extracted IMG_DATA folder as Matlab mat file
import matplotlib.image as mpimg
from scipy.io import savemat
import os

# folder to unzip
Directory = 'E:/Dropbox/Dataset/satellite/sentinel2/'
SentinelGrids = ['35TPF', '35TPE']
ResolutionList = ['R20m','R60m']

# go over the all grids
for gridName in SentinelGrids:
    
    # set the input and output directory
    InputDirectory = os.path.join(Directory, gridName + '_IMGDATA')
    OutputDirectory = os.path.join(Directory, gridName + '_MATDATA')

    # create output directory
    if not os.path.exists(OutputDirectory):
        print('Creating output directory...')
        os.makedirs(OutputDirectory)

    for files in os.listdir(InputDirectory):
        
        # set the output file directory
        InputFileDirectory = os.path.join(InputDirectory, files)
        OutputFileDirectory = os.path.join(OutputDirectory, files)
        
        # create output directory
        if not os.path.exists(OutputFileDirectory):
            print('Creating output file directory...')
            os.makedirs(OutputFileDirectory)
        
        # go over all resolutions
        for resolutions in ResolutionList:
            
            # create array
            images = {}
            print(f'creating {resolutions}.mat for {files}')
            
            for jp in os.listdir(os.path.join(InputFileDirectory, resolutions)):
                if jp.endswith(".jp2"):
                    images[jp[23:26]] = mpimg.imread(os.path.join(InputFileDirectory, resolutions, jp))
        
            # save the image
            savemat(os.path.join(OutputFileDirectory, resolutions + '.mat'), images)
# goodbye
print('Done')
