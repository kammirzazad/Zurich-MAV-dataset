import os
import sys

size = 416
thresh = 0.24
flickerMargin = 2
path2home = '/home/ubuntu/Documents/'
path2images = path2home + 'AGZ/MAV_Images/'
path2darknet = path2home + 'DREML/darknet-nnpack-dreml/'

if len(sys.argv) != 3:
    print('usage:',sys.argv[0],'[neuralnet] [imagelist]')
    exit(1)

net = sys.argv[1]
imageList = sys.argv[2]
assert net in ['yolov2','yolov3','yolov2-tiny','yolov3-tiny']

threshStr = '0_' + str(thresh).split('.')[-1]
path2weight = path2home + 'darknet_weights/' + net + '.weights'
leafDir = net + '-' + imageList.split('.txt')[0].split('AGZ_')[-1]
outputDir = path2home + 'Zurich-MAV-dataset/object-detection/raw/' + str(size) + '/resized/' + threshStr + '/' + leafDir + '/'

print('size:', size)
print('thresh:', thresh)
print('outputDir:', outputDir)
print('path2images:', path2images)
print('path2weight:', path2weight)
print('path2darknet:', path2darknet)
print('flickerMargin:', flickerMargin)

os.system('rm -rf ' + outputDir)
os.system('mkdir ' + outputDir)

with open(imageList,'r') as fh:
    for line in fh:
        baseName = line.split('.txt')[0]
        baseIndex = int(baseName)
        for imIndex in range(baseIndex - flickerMargin, baseIndex + flickerMargin + 1):
            imName = str(imIndex).zfill(5)
            print(imName)
            os.system('cd ' + path2darknet + '/; ./darknet detect -thresh ' + str(thresh) + ' ./cfg/' + net + '.cfg ' + path2weight + ' ' + path2images + '/' + imName + '.jpg 2> /dev/null')
            os.system('cd ' + path2darknet + '/; mv det_result.txt ' + outputDir + '/' + imName + '.txt')
