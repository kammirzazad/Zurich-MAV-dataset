import sys

from glob import glob

if len(sys.argv) != 2:
	print('usage:',sys.argv[0],'[path to truth folder]')
	exit(1)

for fn in glob(sys.argv[1]+'/*.txt'):
	text = ''
	with open(fn,'r') as fh:
		for line in fh:
			words = line.split('\n')[0].split()
			text += words[0] + ' ' 
			text += words[2] + ' '
			text += words[3] + ' '
			text += words[4] + ' '
			text += words[5] + '\n'

	with open(fn,'w') as fh:
		fh.write(text)
