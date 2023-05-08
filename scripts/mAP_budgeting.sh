#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "usage: $0 [net] [latency <1.0]"
    exit 1
fi

NET=$1
LATENCY=$2
SEED="4716771"
PROTOCOL="tcp"
PRINT_COUNT=false
#TRUTHDIR="labelImg/txt"
#TRUTHDIR="edited-yolov3"
TRUTHDIR="consistent/416/0_24/truth-yolov2-30-fps"

RESDIR="../../DREML-data/emulator/"$NET
INPUTDIR="./mAP/input/detection-results/"

print_mAP () {
   echo -e -n "$1   \t"
   DIR=$RESDIR/$PROTOCOL/$SEED/$1/$LATENCY/
   ./get_mAP.sh $DIR
   if $PRINT_COUNT
   then
      ls -l $DIR/*.txt | wc -l
   fi
}


# clear input folders
rm $INPUTDIR/*
rm ./mAP/input/ground-truth/*

# copy ground truth
cp ../Zurich-MAV-dataset/object-detection/$TRUTHDIR/*.txt ./mAP/input/ground-truth/

: '
print_mAP "random/0/memcopy/uniform"
print_mAP "random/0/static/uniform"
'

print_mAP "adaptive/0/static/uniform"
print_mAP "adaptive/1/static/uniform"

: '
print_mAP "adaptive/1/dynamic/uniform"
print_mAP "adaptive/1/dynamic/minsum"
print_mAP "adaptive/1/dynamic/minmax"
'
