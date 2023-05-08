"""
  Script to calculate dice & IoU coefficients for image segementation

  References:
  [1] https://towardsdatascience.com/metrics-to-evaluate-your-semantic-segmentation-model-6bcb99639aa2
  [2] https://stats.stackexchange.com/questions/273537/f1-dice-score-vs-iou/276144#276144
"""
ii = 4
jj = 7 #4

import	sys
import numpy as np
from glob import glob

precision = 4

def	loadData(path2file):
	data = []
	with open(path2file,'r') as fh:
		for line in fh:
			vals = line.split('\n')[0].split()
			for val in vals:
				data.append(int(val))
	return	data

def	getIntersection(label,arr1,arr2):
	intersect = 0
	for i in range(len(arr1)):
		if arr1[i] == label and arr2[i] == label:
			intersect += 1
	return	intersect

def	getUnion(label,arr1,arr2):
	union = 0
	for i in range(len(arr1)):
		if arr1[i] == label or arr2[i] == label:
			union += 1
	return	union

def	getMeanIouScore(intersects,unions,smooth=1):
	scores = []
	for label in unions:
		scores.append(float(intersects[label] + smooth) / (unions[label] + smooth))
	return np.mean(scores)

def	getMeanDiceScore(intersects,unions,smooth=1):
	scores = []
	for label in unions:
		scores.append(float((2 * intersects[label]) + smooth) / (unions[label] + intersects[label] + smooth))
	return np.mean(scores)


if __name__ == "__main__":
	
	if len(sys.argv) != 3:
		print('usage:',sys.argv[0],'[path2result] [path2truth]')
		exit(1)

	iouArr = []
	diceArr = []
	path2truth = sys.argv[2]

	# go over all images
	for fn in sorted(glob(path2truth+'*.txt')): #[2+(25*ii)+jj:2+25*(ii+0)+jj+1]:

		unions = {}
		intersects = {}

		bn = fn.split('/')[-1]
		#print(bn)

		truth = loadData(fn)
		result = loadData(sys.argv[1]+bn)

		# go over all labels
		for label in set(truth):

			assert not label in unions
			assert not label in intersects

			# accumulate unions and intersects
			unions[label] = getUnion(label,result,truth)
			intersects[label] = getIntersection(label,result,truth)

		iouArr.append(getMeanIouScore(intersects,unions))
		diceArr.append(getMeanDiceScore(intersects,unions))

		#if not len(unions) in [14,15,17,18]:
		#	print(bn+', #labels='+str(len(unions)))

	print('meanIoU='+str(round(np.mean(iouArr),precision))+',\t meanDice='+str(round(np.mean(diceArr),precision)))
