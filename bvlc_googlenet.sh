#!/usr/bin/env sh
#
echo "##$1##"
scripts/build/examples/cpp_classification/Release/classification.exe \
models/bvlc_googlenet/deploy.prototxt \
models/bvlc_googlenet/bvlc_googlenet.caffemodel \
data/ilsvrc12/imagenet_mean.binaryproto \
data/ilsvrc12/synset_words_chinese.txt $1
#data/ilsvrc12/synset_words.txt $1

