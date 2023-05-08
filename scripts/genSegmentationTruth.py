import os
import sys

cfg_fn = 'instance_segment.cfg'
weights_fn = 'instance_segment_161000.weights'

inputDir = '../Zurich-MAV-dataset/images/'
path2darknet = '../darknet-nnpack-dreml/'

if len(sys.argv) != 2:
        print('usage:',sys.argv[0],'[imagelist]')
        exit(1)

imageList = sys.argv[1]
inputDir = os.path.abspath(inputDir)
outputDir = os.path.abspath('./iseg/')

os.system('rm -rf ' + outputDir)
os.system('mkdir ' + outputDir)

with open(imageList) as fh:
	for line in fh:
		imName = line.split('.txt')[0]
		print(imName)
		os.system('cd ' + path2darknet + '/; ./darknet segmenter test cfg/maskyolo.data cfg/' + cfg_fn + ' ../../darknet_weights/' + weights_fn + ' ' + inputDir + '/' + imName + '.jpg')
		os.system('cd ' + path2darknet + '/; mv iseg_result.txt ' + outputDir + '/' + imName + '.txt')
