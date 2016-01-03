## The target of this project is to use a python way to classify the mnist test images from png format.


caffe should be installed correctly.

'classification_test_images.py' is the main file.

Something can be specified in it.

like:

dirPath = './test/'
extension = 'png'

net_file = '/home/joe/github/caffe/examples/zy-mnist/zy-deploy-test-net.prototxt'
model_file = '/home/joe/github/caffe/snapshot_iter_2345.caffemodel'

then run it will give output a file contained classification result named 'test_image_classify_Result.npy'

it can be read by using "np.load('test_image_classify_Result.npy')"
