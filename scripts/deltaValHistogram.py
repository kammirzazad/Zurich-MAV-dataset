import	os
import	cv2
import	sys
import	random
import	numpy as np
import	matplotlib.pyplot as plt

from glob import glob

images = '../Zurich-MAV-dataset/images/'

if __name__ == "__main__":

	if len(sys.argv) not in [2,3]:
		print('usage:',sys.argv[0],'[imageList] [index (optional)]')
		exit(1)

	fnArr = []
	with open(sys.argv[1],'r') as fh:
		for line in fh:
			fnArr.append(line.split('\n')[0])

	if len(sys.argv) == 3:
		index = int(sys.argv[2])
	else:
		index = 0

	while True:

		bn = fnArr[index].split('.txt')[0]
		bn2 = fnArr[49].split('.txt')[0]

		print(bn,bn2)

		image =  cv2.resize(cv2.imread(images + bn + '.jpg'),(416,416))
		image2 =  cv2.resize(cv2.imread(images + bn2 + '.jpg'),(416,416))
		image3 = cv2.absdiff(image,image2)

		cv2.imshow('hello',image3)
		k = cv2.waitKeyEx(0)
		cv2.destroyWindow('hello')

		"""
		vals = []
		maxVal = 25

		for x in range(image.shape[0]):
			for y in range(image.shape[1]):
				for c in range(image.shape[2]):
					if image[x][y][c] == 0:
						vals.append(maxVal)
					else:
						val = abs((image2[x][y][c]/image[x][y][c])-1)
						if val > maxVal:
							val = maxVal
						vals.append(val)

		plt.clf()
		plt.hist(vals, density=True, bins=1000)  # density=False would make counts
		plt.ylabel('Probability')
		plt.xlabel('Data')
		plt.show()
		#plt.savefig('histogram.pdf')
		"""

		"""
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
		"""

		index += 1
