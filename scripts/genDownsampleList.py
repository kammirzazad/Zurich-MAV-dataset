import	sys

if len(sys.argv) != 3:
    print('usage:', sys.argv[0], '[fps]', '[numFrames]')
    exit(1)

fps = int(sys.argv[1])
numFrames = int(sys.argv[2])

assert fps < 30, 'baseline fps is 30'

maxIndex = 81169
startIndex = 32000

indice = []
for i in range(numFrames):
    index = int(startIndex + i * (30 / fps))
    if index > maxIndex:
        print('there are only ', i, 'frames @', fps, 'fps')
        break
    indice.append(index)

fn = '../imagelists/AGZ_' + str(fps) + '_fps_' + str(numFrames) + '.txt'
with open(fn, 'w') as fh:
    for index in indice:
        fh.write(str(index).zfill(5)+'.txt\n')
