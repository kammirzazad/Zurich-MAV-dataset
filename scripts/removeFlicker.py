import	sys
from	glob import glob

def	getSize(det):
	return	(det['right']-det['left']+1) * (det['bot']-det['top']+1)


def	loadDets(fn):
	dets = []
	with open(fn,'r') as fh:
		for line in fh:
			data = line.split()
			#print(data)
			dets.append({'name':data[0], 'prob':float(data[1]), 'left':int(data[2]), 'top':int(data[3]), 'right':int(data[4]), 'bot':int(data[5])})
	return	dets


def	getIntersect(det0,det1):
	assert det0['name'] == det1['name']
	intersect = {'name':det0['name']}
	intersect['left'] = max(det0['left'],det1['left'])
	intersect['right'] = min(det0['right'],det1['right'])
	intersect['top'] = max(det0['top'],det1['top'])
	intersect['bot'] = min(det0['bot'],det1['bot'])

	if intersect['left'] > intersect['right']:
		intersect['right'] = intersect['left'] - 1

	if intersect['top'] > intersect['bot']:
		intersect['bot'] = intersect['top'] - 1

	return	intersect


def	getIoU(currDet,dets):
	maxIoU = 0.0
	for det in dets:
		if currDet['name'] == det['name']:
			intersectSize = getSize(getIntersect(currDet,det))
			unionSize = getSize(currDet) + getSize(det) - intersectSize
			currIoU = float(intersectSize) / float(unionSize)
			if currIoU > maxIoU:
				maxIoU = currIoU
	return	maxIoU
	
		
def	isConsistent(i,thresh,currDet,files,count):
	det_i_next = []
	det_i_prev = []
	
	for idx in range(1,count):
	
		if i < len(files) - idx:
			dets = loadDets(files[i+idx])
			det_i_next.append(getIoU(currDet,dets) > thresh)
		else:
			det_i_next.append(True)

		if i >= idx:
			dets = loadDets(files[i-idx])
			det_i_prev.append(getIoU(currDet,dets) > thresh)
		else:
			det_i_prev.append(True)

	return	(det_i_prev[1] and det_i_prev[0]) or (det_i_prev[0] and det_i_next[0]) or (det_i_next[0] and det_i_next[1])

	"""
	# hardcoded part
	assert count == 5
	return	(det_i_prev[3] and det_i_prev[2] and det_i_prev[1] and det_i_prev[0]) or\
		(det_i_prev[2] and det_i_prev[1] and det_i_prev[0] and det_i_next[0]) or\
		(det_i_prev[1] and det_i_prev[0] and det_i_next[0] and det_i_next[1]) or\
		(det_i_prev[0] and det_i_next[0] and det_i_next[1] and det_i_next[2]) or\
		(det_i_next[0] and det_i_next[1] and det_i_next[2] and det_i_next[3])
	"""


if __name__ == "__main__":

	if len(sys.argv) not in [3,4]:
		print('usage:',sys.argv[0],'[path2folder] [thresh] [debug (opt)]')
		exit(1)

	debug = (len(sys.argv)==4)
	thresh = float(sys.argv[2])
	files = sorted(glob(sys.argv[1]+'/*.txt'))

	for i in range(len(files)):
		dets = loadDets(files[i])
		with open(files[i],'w') as fh:
			for currDet in dets:
				if isConsistent(i,thresh,currDet,files,3):
					fh.write(currDet['name']+' '+str(currDet['prob'])+' '+str(currDet['left'])+' '+str(currDet['top'])+' '+str(currDet['right'])+' '+str(currDet['bot'])+'\n')
				elif debug:
					print('removed',currDet['name'],'from',files[i])
