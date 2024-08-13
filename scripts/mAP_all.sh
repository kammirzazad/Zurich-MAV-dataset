#!/bin/bash

if [ "$#" -ne 9 ]; then
   echo "usage: $0 [net] [latency <1.0] [gridSize] [updateFreq] [layerGroups] [seed] [metric] [onlyFullOpt] [queueSize]"
   exit 1
fi

NET=$1
LATENCY=$2
GRIDSIZE=$3
UPDATEFREQ=$4
LAYERGROUPS=$5
SEED=$6
METRIC=$7
ONLYFULLOPT=$8
QUEUESIZE=$9
PRINT_COUNT=false

TRUTH_TYPE="raw"
#TRUTH_TYPE="consistent"

if [ "$NET" = "YOLOv2" ]; then
   TRUTH_DIR="${TRUTH_TYPE}/416/resized/0_24/truth-yolov2-1-fps"
elif [ "$NET" = "YOLOv3" ]; then
   TRUTH_DIR="${TRUTH_TYPE}/416/resized/0_24/truth-yolov3-1-fps"
else
   echo Unknown network ${NET}
   exit 1
fi

RESDIR=$(realpath ~/Documents/DREML-data/simulator/)

print_mAP () {
   SETTING=$1
   if [ ${ONLYFULLOPT} = "0" ]; then
      # no need to print setting with full-opt
      echo -e -n "$1   \t"
   fi
   DIR="${RESDIR}/${NET}/${METRIC}/${QUEUESIZE}/${GRIDSIZE}/${UPDATEFREQ}/${LAYERGROUPS}/tcp/${SEED}/${SETTING}/${LATENCY}/"
   #./get_mAP.sh $DIR
   python3 interval_mAP.py $DIR ${QUEUESIZE}
   if $PRINT_COUNT
   then
      ls -l $DIR/*.txt | wc -l
   fi
}

# clear input folders
rm ./mAP/input/ground-truth/*
rm ./mAP/input/detection-results/*

# copy ground truth
rm -rf /tmp/truth/
mkdir -p /tmp/truth/
cp ../object-detection/${TRUTH_DIR}/*.txt /tmp/truth/

#rm ./mAP/input/ground-truth/32150.txt ./mAP/input/ground-truth/32180.txt ./mAP/input/ground-truth/32210.txt ./mAP/input/ground-truth/32240.txt ./mAP/input/ground-truth/32270.txt

if [ ${ONLYFULLOPT} = "0" ]; then
   print_mAP "random/0/memcopy/uniform"
   print_mAP "adaptive/0/memcopy/uniform"
   print_mAP "adaptive/1/memcopy/uniform"
   print_mAP "adaptive/1/static/uniform"
   print_mAP "adaptive/1/dynamic/uniform"
fi

print_mAP "adaptive/1/dynamic/minmax"
