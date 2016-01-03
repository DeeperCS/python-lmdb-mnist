'''
This example is to show how to use os module to
iterate the sub-folders and sub-files

Ex: using 'dirPath' as target folder, iterate the sub-folder in 'dirPath'
find out all files with 'extension' specified
'''

import sys
sys.path.insert(0,'/home/joe/github/caffe/python')
from PIL import Image
import os
import glob
import numpy as np
import caffe

# list all files under 'dirPath', like the bash cmd 'ls'
# ./test
#	./0/
#	./1/
#	./2/
#	./.../
dirPath = './test/'
extension = 'png'

net_file = '/home/joe/github/caffe/examples/zy-mnist/zy-deploy-test-net.prototxt'
model_file = '/home/joe/github/caffe/snapshot_iter_2345.caffemodel'
    
fileList = os.listdir(dirPath)

filePathList = []
for filename in fileList:
    path = os.path.join(dirPath, filename)
    # consider only folders    
    if os.path.isdir(path):
        # Using glob to find all files with specified extension in sub-folders
        files_list_in_one_folder = glob.glob(path+"/*."+extension)
        filePathList.append(files_list_in_one_folder)

# concatenate them and turn to ndarray
filePathListNp = np.concatenate(filePathList)

'''
Using caffe to classify test images
and save result to 'classifyResult.npy'
format: (filename, category)
you can read it by np.load('classifyResult.npy')
'''

# using caffemodel to classify the images
classifyResult = []
for idx, im_path in enumerate(filePathListNp):
    im = Image.open(im_path)
    in_ = np.array(im, dtype=np.float32)
    
    # deal with gray images
    if len(in_.shape)== 2:
        in_ = np.reshape(in_, ([in_.shape[0], in_.shape[1], 1]))
        
    in_ = in_[:,:,::-1]
    in_ = in_.transpose((2,0,1))
    
    # load net
    net = caffe.Net(net_file, model_file, caffe.TEST)
    # shape for input (data blob is N x C x H x W), set data
    net.blobs['data'].reshape(1, *in_.shape)
    net.blobs['data'].data[...] = in_
    
    # run net and take argmax for prediction
    net.forward()
    out = net.blobs['prob'].data[0].argmax(axis=0)
    classifyResult.append((im_path, out))
    
    # save result
    np.save('test_image_classify_Result.npy', classifyResult)
    
    # I really don't know how to disable caffe's logging information - -
    if idx%1000 == 0:
            string_ = str(idx+1) + ' / ' + str(len(filePathListNp))
            sys.stdout.write("\r%s" % string_)
            sys.stdout.flush()
