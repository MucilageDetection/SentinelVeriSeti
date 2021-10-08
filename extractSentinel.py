# Bahri ABACI
# Extract Sentinel images from zip file and put them into folder
import zipfile
import shutil
import glob
import os

# folder to unzip
Directory = 'E:/Dropbox/Dataset/satellite/sentinel2/'
SentinelGrids = ['35TPF', '35TPE']

# go over the all grids
for gridName in SentinelGrids:
    
    # set the input and output directory
    InputDirectory = os.path.join(Directory, gridName)
    OutputDirectory = os.path.join(Directory, gridName + '_IMGDATA')

    # get the all zip files under the given path
    zippedFileName = os.listdir(InputDirectory)
    print(f'{len(zippedFileName)} zip files found in {gridName} directory')

    # create output directory
    if not os.path.exists(OutputDirectory):
        print('Creating output directory...')
        os.makedirs(OutputDirectory)
        
    # delete temp if it exist
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    
    # unzip each zip file in given directory
    for idx, zippedFile in enumerate(zippedFileName):
        # print the status
        print(f'[{idx+1:03} / {len(zippedFileName)}] Unzipping {zippedFile}...')
        
        # unzip if not
        DestPath = os.path.join(OutputDirectory, os.path.splitext(zippedFile)[0])
        if not os.path.exists(DestPath):
        
            # create temp directory for unzip
            os.makedirs('temp')
            
            # do unzipping
            with zipfile.ZipFile(os.path.join(InputDirectory, zippedFile), "r") as zipRef:
                zipRef.extractall('temp')
    
            # find the R60m folder
            for root, subdirs, files in os.walk('temp'):
                for d in subdirs:
                    if d == 'IMG_DATA':
                        # move the directory to the final destination
                        SrcPath = os.path.join(root, d)
                        print(f'Moving {SrcPath} to {DestPath} ...')
                        os.rename(SrcPath, DestPath)
    
            # remove temp
            shutil.rmtree('temp')
        else:
            print(f'{zippedFile} already extracted!')

# goodbye
print('Done')
