import caffe
import numpy as np
root = 'D:/Study/caffe-windows/'
mnist = root + 'examples/mnist/'
deploy = mnist + 'lenet_train_test.prototxt'
caffe_model = mnist + 'lenet_iter_10000.caffemodel'

net = caffe.Net(deploy,caffe_model,caffe.TEST)

net.forward()

import os

caffe_out = mnist + 'caffe_out/'

isExists = os.path.exists(caffe_out)

if not isExists:
    os.makedirs(caffe_out)

params = net.params
#save every layer weight and bias
for layer in params:
	filename = caffe_out + layer + '_weight.txt'
	fd = open(filename, 'w')
	w = params[layer][0].data
	w = w.reshape(w.size)
	size = w.size
	for i in range(size):
		fd.write(str(w[i]))
		fd.write('\n')
	fd.close
	
	filename = caffe_out + layer + '_bias.txt'
	fd = open(filename, 'w')
	w = params[layer][1].data
	w = w.reshape(w.size)
	size = w.size
	for i in range(size):
		fd.write(str(w[i]))
		fd.write('\n')
	fd.close

blobs = net.blobs
#save every layer data
for layer in blobs:
	filename = caffe_out + layer + '_data.txt'
	fd = open(filename, 'w')
	w = blobs[layer].data
	w = w.reshape(w.size)
	size = w.size
	for i in range(size):
		fd.write(str(w[i]))
		fd.write('\n')
	fd.close	
