import	sys

imWidth = 1920
imHeight = 1080

raw_files = './raw/'
txt_files = './txt/'

def	loadFile(fn):
	allData = []
	with open(fn,'r') as fh:
		for line in fh:
			data = line.split('\n')[0].split()
			if len(data) == 1:
				allData.append(data[0])
			elif len(data) == 2:
				allData.append(data[0]+'_'+data[1])
	return	allData


if len(sys.argv) != 3:
	print('usage:',sys.argv[0],'[imagelist] [classfile]')
	exit(1)

images = loadFile(sys.argv[1])
classes = loadFile(sys.argv[2])

for image in images:

	raw_fh = open(raw_files+image,'r')
	txt_fh = open(txt_files+image,'w')

	for line in raw_fh:
		data = line.split('\n')[0].split()

		classId = int(data[0])
		x = float(data[1])
		y = float(data[2])
		w = float(data[3])
		h = float(data[4])

		left  = (x - w/2.0) * imWidth
		right = (x + w/2.0) * imWidth
		top   = (y - h/2.0) * imHeight
		bot   = (y + h/2.0) * imHeight

		if left < 0:
			left = 0

		if right > imWidth-1:
			right = imWidth-1

		if top < 0:
			top = 0

		if bot > imHeight-1:
			bot = imHeight-1;

		# left, top, right, bot
		txt_fh.write(classes[classId]+' '+str(left)+' '+str(top)+' '+str(right)+' '+str(bot)+'\n')
	
	raw_fh.close()
	txt_fh.close()
