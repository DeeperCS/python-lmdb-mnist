'''
This example is to show how to use os module to
iterate the sub-folders and sub-files

Ex: using 'dirPath' as target folder, iterate the sub-folder in 'dirPath'
find out all files with 'extension' specified
'filePathListNp' return all file pathes corresponding to the conditions given above
'''

import os
import glob
import numpy as np
from random import shuffle

# list all files under 'dirPath', like the bash cmd 'ls'
dirPath = './test/'
extension = 'png'
fileList = os.listdir(dirPath)

filePathList = []
for filename in fileList:
    path = os.path.join(dirPath, filename)
    # only show folders    
    if os.path.isdir(path):
        # Things to do with sub-folders
        pass
        print("reading from directory: {}".format(filename))
#        files_list_in_one_folder = sorted(glob.glob(path+"/*."+extension))
        files_list_in_one_folder = glob.glob(path+"/*."+extension)
        filePathList.append(files_list_in_one_folder)
            
    elif os.path.isfile(path):
        # Things to do with sub-files
        pass
        print("reading file: {}".format(filename))
        
filePathListNp = np.concatenate(filePathList)

#shuffle(filePathListNp)