# Bahri ABACI
# Extract Sentinel images from zip file and put them into folder
from pgmagick import Image
import os

# folder to unzip
InputDirectory = '35TPF_IMGDATA'
OutputDirectory = '35TPF_TCI_TABLE'

# create output directory
if not os.path.exists(OutputDirectory):
    print('Creating output directory...')
    os.makedirs(OutputDirectory)
    
# get the all jp2 files under the given path
markdownOrder = []
markdownDate = []
markdownImage = []

for root, subdirs, files in os.walk(InputDirectory):
    for f in files:
        if 'TCI' in f:
            # T35TPF_20200815T085601_TCI_60m
            print(f'Converting {f} to jpeg ...')
            
            # do the jp2 to jpeg conversion
            SrcPath = os.path.join(root, f)
            DestPath = os.path.join(OutputDirectory, os.path.splitext(f)[0] + '.jpg')
            TCI = Image(SrcPath)
            TCI.write(DestPath)
            
            # add the elements to the list
            YearMonthDay = 10000 * int(f[7:11]) + 100 * int(f[11:13]) + int(f[13:15])
            DayMonthYear = f[13:15] + '-' + f[11:13] + '-' + f[7:11]
            markdownOrder.append(YearMonthDay)
            markdownDate.append(DayMonthYear)
            markdownImage.append(f'![{DayMonthYear}]({DestPath})')
            

# sort the elements
markdownDate = [x for _,x in sorted(zip(markdownOrder,markdownDate))]
markdownImage = [x for _,x in sorted(zip(markdownOrder,markdownImage))]

######## Create Markdown File
rowCounter = 0
maxRowCounter = 5

mdHeader = '|'
mdSeperator = '|'
mdRowDates = '| '
mdRowImages = '| '

# open the table file
markdownFile = open("TCITable.md", "w")

for i in range(maxRowCounter):
    mdHeader = mdHeader + ' |'
    mdSeperator = mdSeperator + ':-------:|'

markdownFile.writelines([mdHeader + '\n', mdSeperator + '\n'])

# print the results
for i in range(len(markdownOrder)):
    
    # create row
    mdRowDates = mdRowDates + markdownDate[i] + '|'
    mdRowImages = mdRowImages + markdownImage[i] + '|'
    
    rowCounter = rowCounter + 1
    if rowCounter == maxRowCounter:
        rowCounter = 0
        markdownFile.writelines([mdRowDates + '\n', mdRowImages + '\n'])
        mdRowDates = '| '
        mdRowImages = '| '

if rowCounter != 0:
    markdownFile.writelines([mdRowDates + '\n', mdRowImages + '\n'])
    
# close the file
markdownFile.close()

# goodbye
print('Done')
