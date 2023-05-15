import  os
import  sys
from glob import glob


if len(sys.argv) != 3:
    print('usage:', sys.argv[0], '[imagelist]', '[path2data]')
    exit(1)

images = []
with open(sys.argv[1], 'r') as fh:
    for line in fh:
        images.append(line.split('\n')[0])

files = list(glob(sys.argv[2] + '/*.txt'))
for file in files:
    bn = file.split('/')[-1]
    if bn not in images:
        # print('removing', bn)
        os.system('rm ' + file)
    else:
        print('keeping', bn)
