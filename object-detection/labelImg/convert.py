import	sys

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
		txt_fh.write(classes[classId]+' '+data[1]+' '+data[2]+' '+data[3]+' '+data[4]+'\n')
	
	raw_fh.close()
	txt_fh.close()
