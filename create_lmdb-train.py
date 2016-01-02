# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:07:50 2016

@author: joe
"""
import numpy as np
import fileinput, re
import lmdb
from PIL import Image

# Make sure that caffe is on the python path:
caffe_root = 'home/joe/github/caffe/'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

data = 'train.txt'
lmdb_data_name = 'train_data_lmdb'
lmdb_label_name = 'train_label_lmdb'

Inputs = []
Labels = []

for line in fileinput.input(data):
	entries = re.split(' ', line.strip())
	Inputs.append(entries[0])
	Labels.append(entries[1])

# Labels
print('Creating {}'.format(lmdb_label_name))
in_db = lmdb.open(lmdb_label_name, map_size=int(1e12))
with in_db.begin(write=True) as in_txn:
    for in_idx, in_ in enumerate(Labels):
        # load label:
        # - as np.uint8
        # - in float and reshape
        label = np.array(in_).astype(float).reshape(1,1,1)

        # - Turn to caffe object
        label_dat = caffe.io.array_to_datum(label)

        # - Write it
        in_txn.put('{:0>10d}'.format(in_idx), label_dat.SerializeToString())

        # - print information
        if in_idx%1000 == 0:
            string_ = str(in_idx+1) + ' / ' + str(len(Inputs))
            sys.stdout.write("\r%s" % string_)
            sys.stdout.flush()
in_db.close()

# Data
print('Creating {}'.format(lmdb_data_name))
in_db = lmdb.open(lmdb_data_name, map_size=int(1e12))
with in_db.begin(write=True) as in_txn:
    for in_idx, in_ in enumerate(Inputs):
        # load image:
        # - as np.uint8 {0, ..., 255}
        im = np.array(Image.open(in_)) # or load whatever ndarray you need

        # if gray images, reshape to HxWx1
        if len(im.shape) == 2:
            im = np.reshape(im, ([im.shape[0], im.shape[1], 1]))

        # - in BGR (switch from RGB)
        im = im[:,:,::-1]

        # - in Channel x Height x Width order (switch from H x W x C)
        im = im.transpose((2,0,1))

        # - Turn to caffe object
        im_dat = caffe.io.array_to_datum(im)

        # - Write it
        in_txn.put('{:0>10d}'.format(in_idx), im_dat.SerializeToString())

        # - print information
        if in_idx%1000 == 0:
            string_ = str(in_idx+1) + ' / ' + str(len(Inputs))
            sys.stdout.write("\r%s" % string_)
            sys.stdout.flush()
in_db.close()
