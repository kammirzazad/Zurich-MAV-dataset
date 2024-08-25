import  os
import  sys
import  subprocess

fps = 30
interval_size = 200
batch_size = interval_size
min_index = 32000
max_index = min_index + (fps * interval_size) #47000
input_dir = "./mAP/input/detection-results/"
ground_truth = "./mAP/input/ground-truth/"
interval_input = "/tmp/det/"
interval_truth = "/tmp/truth/"

if len(sys.argv) != 3:
    print(sys.argv[0], '[path_to_input]', '[queue_size]')
    exit(1)

queue_size = int(sys.argv[2])

# interval_truth is handled in mAP_all.sh
os.system("rm -rf " + interval_input)
os.system("mkdir -p " + interval_input)
os.system("cp " + sys.argv[1] + "/*.txt " + interval_input)

vals = []
for i in range(min_index, max_index, (fps * batch_size)):
    os.system("rm " + input_dir + "/* " + ground_truth + "/* 2> /dev/null")

    for j in range(i, min(i + (fps * batch_size), max_index), fps):
        if j < min_index + (queue_size * fps):
            continue
        os.system("cp " + interval_input + str(j) + ".txt " + input_dir)
        os.system("cp " + interval_truth + str(j) + ".txt " + ground_truth)

    os.system("python3 remove_space.py " + input_dir)
    val = subprocess.run(["python3", "./mAP/main.py", "-na", "-np", "-q"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    val = float(val.split('mAP = ')[1].split('%')[0])
    vals.append(val)

print(vals)
