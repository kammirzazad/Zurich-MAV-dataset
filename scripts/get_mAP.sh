#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "usage: $0 [path2results]"
    exit 1
fi

INPUTDIR="./mAP/input/detection-results/"

rm $INPUTDIR/* 2> /dev/null
cp $1/*.txt $INPUTDIR
python3 remove_space.py $INPUTDIR
#python3 ../Zurich-MAV-dataset/object-detection/removeFlicker.py $INPUTDIR 0.5
python3 ./mAP/main.py -na -np -q
