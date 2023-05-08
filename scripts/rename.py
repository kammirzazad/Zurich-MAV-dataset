import	os
import	sys
import	glob

files = glob.glob(sys.argv[1]+'/*.txt')
for fn in files:
	fn2 = fn.split('AGZ')[0] + fn.split('_')[-1]
	os.system('mv '+fn+' '+fn2)
