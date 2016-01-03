'''
This example is to show how to use os module to
iterate the sub-folders and sub-files
'''

import os

# list all files under 'dirPath', like the bash cmd 'ls'
dirPath = './train/'
fileList = os.listdir(dirPath)

for filename in fileList:
    path = os.path.join(dirPath, filename)
    # only show folders    
    if os.path.isdir(path):
        # Things to do with sub-folders
        pass
        print("directory: {}".format(filename))
    elif os.path.isfile(path):
        # Things to do with sub-files
        pass
        print("file: {}".format(filename))