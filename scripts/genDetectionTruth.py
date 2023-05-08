import os
import sys

inputDir = '../Zurich-MAV-dataset/images/'
path2darknet = '../darknet-nnpack-dreml/'

if len(sys.argv) != 4:
    print('usage:',sys.argv[0],'[neuralnet] [thresh] [imagelist]')
    exit(1)

net = sys.argv[1]
thresh = float(sys.argv[2])
imageList = sys.argv[3]
assert net in ['yolov2','yolov3','yolov2-tiny','yolov3-tiny']

inputDir = os.path.abspath(inputDir)
outputDir = os.path.abspath('./'+net+'/')

os.system('rm -rf '+outputDir)
os.system('mkdir '+outputDir)

with open(imageList,'r') as fh:
	for line in fh:
		imName = line.split('.txt')[0]
		print(imName)
		os.system('cd ' + path2darknet + '/; ./darknet detect -thresh ' + str(thresh) + ' ./cfg/' + net + '.cfg ../../darknet_weights/' + net + '.weights ' + inputDir + '/' + imName + '.jpg 2> /dev/null')
		os.system('cd ' + path2darknet + '/; mv det_result.txt ' + outputDir + '/' + imName + '.txt')
