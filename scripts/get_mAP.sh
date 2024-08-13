#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "usage: $0 [path2results]"
    exit 1
fi

INPUTDIR="./mAP/input/detection-results/"
IMAGELIST="../imagelists/AGZ_1_fps_500.txt"
REFDIR="../object-detection/raw/416/resized/0_24/yolov3-1-fps-500/"

rm ${INPUTDIR}/* 2> /dev/null
#cp ${REFDIR}/*.txt ${INPUTDIR}
cp $1/*.txt ${INPUTDIR}
python3 remove_space.py ${INPUTDIR}
#python3 remove_flicker.py ${INPUTDIR} ${IMAGELIST}
#python3 remove_extra_data.py ${IMAGELIST} ${INPUTDIR} 
#rm ${INPUTDIR}/32000.txt ${INPUTDIR}/32030.txt ${INPUTDIR}/32060.txt ${INPUTDIR}/32090.txt ${INPUTDIR}/32120.txt
# just first 200 frames
#rm ${INPUTDIR}/38*.txt ${INPUTDIR}/39*.txt ${INPUTDIR}/40*.txt ${INPUTDIR}/41*.txt ${INPUTDIR}/42*.txt ${INPUTDIR}/43*.txt ${INPUTDIR}/44*.txt ${INPUTDIR}/45*.txt ${INPUTDIR}/46*.txt
python3 ./mAP/main.py -na -np -q
