import sys
from glob import glob

if len(sys.argv) != 2:
	print('usage:',sys.argv[0],'[path to folder]')
	exit(1)

for fn in glob(sys.argv[1]+'/*.txt'):

	lines = []
	lines2 = []

	with open(fn,'r') as fh:
		for line in fh:
			lines.append(line.split('\n')[0])

	for line in lines:
		newLine = line.replace('teddy bear', 'teddy_bear')
		newLine = newLine.replace('wine glass', 'wine_glass')
		newLine = newLine.replace('baseball bat', 'baseball_bat')
		newLine = newLine.replace('traffic light', 'traffic_light')
		newLine = newLine.replace('cell phone', 'cell_phone')
		newLine = newLine.replace('baseball glove', 'baseball_glove')
		newLine = newLine.replace('tennis racket', 'tennis_racket')
		newLine = newLine.replace('sports ball', 'sports_ball')
		newLine = newLine.replace('hot dog', 'hot_dog')
		newLine = newLine.replace('stop sign', 'stop_sign')
		newLine = newLine.replace('fire hydrant', 'fire_hydrant')
		newLine = newLine.replace('parking meter', 'parking_meter')
		newLine = newLine.replace('hair drier', 'hair_drier')
		lines2.append(newLine)
	
	with open(fn,'w') as fh:
		for line in lines2:
			fh.write(line+'\n')
