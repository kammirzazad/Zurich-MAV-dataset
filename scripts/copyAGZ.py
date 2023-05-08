#!/usr/bin/python

import	os
import	sys

files = 'AGZ_slow.txt'

with open(files,'r') as fh:
	for line in fh:
		bn = line.split('.txt')[0]
		os.system('cp truth-yolov2/'+bn+'.txt /home/osboxes/Documents/mAP/input/ground-truth/')
		os.system('cp yolov2/'+bn+'.txt /home/osboxes/Documents/mAP/input/detection-results/')
		#os.system('cp '+lat+'/images/'+bn+'.jpg ./temp/')
