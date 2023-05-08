import	os
import	cv2
import	sys
import	random
from glob import glob

# parameters
net = 'YOLOv2'
size = '416'
seed = '4716771'
isRaw = False
thresh = '0_24'
version = 'yolov2-30-fps'
showResult = True

# other stuff
images = '../Zurich-MAV-dataset/images/'
resultDir = '../../DREML-data/emulator/' + net + '/tcp/' + seed + '/'
truth = '../Zurich-MAV-dataset/object-detection/' + ('raw' if isRaw else 'consistent') + '/' + size + '/' + thresh + '/truth-' + version + '/'

def	annotate(path,fn,image,color,thickness,printLabels,isTruth=False):
	lineType = 2
	fontScale = .5
	font = cv2.FONT_HERSHEY_SIMPLEX

	with open(path+fn) as fh:
		for line in fh:
			vals = line.split()

			if printLabels:
				print(vals)

			offset = 0 if isTruth else 1
			x1 = int(vals[offset+1]) + int(random.uniform(-5,5))
			y1 = int(vals[offset+2]) + int(random.uniform(-5,5))
			x2 = int(vals[offset+3]) + int(random.uniform(-5,5))
			y2 = int(vals[offset+4]) + int(random.uniform(-5,5))
			#print x1,y1,x2,y2
			if vals[0]=='pottedplant':
				vals[0]='pp'
			if True: #not vals[0] in ['car','person','pottedplant']:
				cv2.putText(image,vals[0]+'*'+vals[1],(x1+10,y1-15),font,fontScale,color,lineType)
			cv2.rectangle(image,(x1,y1),(x2,y2),color=color,thickness=thickness)


if __name__ == "__main__":

	if not len(sys.argv) in [3,4]:
		print('usage:',sys.argv[0],'[imageList] [lat] [index(optional)]')
		exit(1)

	if showResult:
		baseline_scheme = 'adaptive/0/static/uniform/' + sys.argv[2]
		optimized_scheme = 'adaptive/1/static/uniform/' + sys.argv[2]

		print('baseline-scheme='+baseline_scheme)
		print('optimized-scheme='+optimized_scheme)

		os.system('python3 remove_space.py '+resultDir+baseline_scheme+'/')
		os.system('python3 remove_space.py '+resultDir+optimized_scheme+'/')
	
		os.system('python3 ../Zurich-MAV-dataset/object-detection/removeFlicker.py '+resultDir+baseline_scheme+'/ 0.5')
		os.system('python3 ../Zurich-MAV-dataset/object-detection/removeFlicker.py '+resultDir+optimized_scheme+'/ 0.5')

	fnArr = []
	with open(sys.argv[1],'r') as fh:
		for line in fh:
			fnArr.append(line.split('\n')[0])

	if len(sys.argv) == 4:
		index = int(sys.argv[3])
	else:
		index = 0

	while(True):

		fn = fnArr[index]

		print('@'+str(index)+':', fn)

		bn = fn.split('.txt')[0]

		image = cv2.imread(images + bn + '.jpg')

		#print image.shape

		annotate(truth,fn,image,(0,255,0),3,True,True) #green

		if showResult:
			annotate(resultDir+baseline_scheme+'/',fn,image,(255,0,0),3,False) #blue
			annotate(resultDir+optimized_scheme+'/',fn,image,(0,0,255),3,False) #red

		image2 = cv2.resize(image,(1000,600))

		cv2.imshow(bn,image2)

		k = cv2.waitKeyEx(0)

		cv2.destroyWindow(bn)

		if k == 97:	# left key 97/81/49
			if index!=0:
				index -= 1
		elif k == 119:	# up key 119/82/50
			index = len(fnArr)-1;
		elif k == 100:	# right key 100/83/51
			if index!=len(fnArr)-1:
				index += 1 
		elif k == 115:	# down key 115/84/52
			index = 0
		else:
			#print(k)
			exit(1)
