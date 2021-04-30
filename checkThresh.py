#!/usr/bin/python

import	sys
from	glob	import	glob
from	pprint	import	pprint
import	matplotlib.pyplot as plt

data = {}
confs_x = {}
confs_y = {}

for fn in sorted(glob(sys.argv[1]+'/*.txt')):
	with open(fn,'r') as fh:
		for line in fh:
			vals = line.split('\n')[0].split()
			obj = vals[0]
			conf = float(vals[1])
			#if conf < 0.4:
			#	continue
			#if conf > 0.5:
			#	continue

			if not obj in data:
				data[obj] = []
				confs_x[obj] = []
				confs_y[obj] = []

			data[obj].append(conf)
			confs_x[obj].append(int(fn.split('.')[0].split('/')[-1].split('AGZ_')[-1]))
			confs_y[obj].append(conf)

"""
for obj in data:
	print(obj,data[obj])
	print()
"""

for obj in data:
	plt.clf()
	plt.scatter(confs_x[obj],confs_y[obj])
	#plt.hist(data[obj], density=True, bins=1000)  # density=False would make counts
	plt.ylabel('conf')
	plt.xlabel('frame')
	#plt.show()
	plt.savefig(obj+'.pdf')
