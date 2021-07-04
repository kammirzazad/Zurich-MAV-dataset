import	sys

rate = int(sys.argv[1])
maxFrame = 81169

indice = []
for index in range(0,maxFrame+1,rate):
	indice.append(index)

with open('AGZ_downsampled_'+str(rate)+'.txt','w') as fh:
	for index in indice[-200:]:
		fh.write(str(index).zfill(5)+'.txt\n')
