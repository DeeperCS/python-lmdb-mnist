To create the mnist's lmdb database using python

1. use the digits's data example
run digits/tools/download_data/main.py mnist ~/mnist to download the mnist dataset
https://github.com/NVIDIA/DIGITS/blob/master/docs/GettingStarted.md

2. mnist will be download to ~/mnist and generate the train.txt and label.txt file dynamicly, the filepath is corresponding to your download location.

3. put create_lmdb-train.py to the folder of ~/mnist/train, then python create_lmdb-train.py to run it.
Remember to setting caffe python interface path in create_lmdb-train.py to make it run correctly.
create_lmdb-train.py will read the train.txt and read the filenames and labels to create two lmdb files.

4. create a train-lenet.prototxt to specify the input data layer and input label layer, use lmdb as their data input.
Beware of the 
  transform_param {
    scale: 0.00390625
  }
it is use for turn the image intensity scope from [0,255] to [0,1], shoud not be used for labels.

Notice that at the end of the network definition file, there is no softmax layer, only a softmax loss layer instead to generate output in terminal logs.
layer {
  name: "loss"
  type: "SoftmaxWithLoss"
  bottom: "ip2"
  bottom: "label"
  top: "loss"
}
This layer means to use the ip2 as input, and softmax it to compare with label to get the cross-entropy loss.

5. create a train-solver.prototxt to sepcify the parameters used for training.

6. create a bash script to avoid type too many command in terminal. ^ ^
