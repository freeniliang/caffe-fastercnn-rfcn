#!/usr/bin/env sh
#
echo "##$1##"
scripts/build/examples/cpp_classification/Release/classification.exe \
models/bvlc_reference_rcnn_ilsvrc13/deploy.prototxt \
models/bvlc_reference_rcnn_ilsvrc13/bvlc_reference_rcnn_ilsvrc13.caffemodel \
data/ilsvrc12/imagenet_mean.binaryproto \
data/ilsvrc12/synset_words_chinese.txt $1
#data/ilsvrc12/synset_words.txt $1

