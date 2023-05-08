#!/bin/bash

if [ "$#" -ne 7 ]; then
    echo "usage: $0 [net] [impactMetric] [queueSize] [latency <1.0] [gridSize] [updateFreq] [layerGroups]"
    exit 1
fi

NET=$1
METRIC=$2
QUEUESIZE=$3
LATENCY=$4
GRIDSIZE=$5
UPDATEFREQ=$6
LAYERGROUPS=$7
SEED="4716771"
PROTOCOL="tcp"
PRINT_COUNT=false
#TRUTHDIR="labelImg/txt"
#TRUTHDIR="edited-yolov3"
TRUTHDIR="consistent/416/resized/0_24/truth-yolov3-30-fps"

RESDIR=$(realpath ~/Documents/DREML-data/simulator/)

print_mAP () {
   echo -e -n "$1   \t"
   DIR="${RESDIR}/${NET}/${METRIC}/${QUEUESIZE}/${GRIDSIZE}/${UPDATEFREQ}/${LAYERGROUPS}/${PROTOCOL}/${SEED}/$1/${LATENCY}/"
   ./get_mAP.sh $DIR
   if $PRINT_COUNT
   then
      ls -l $DIR/*.txt | wc -l
   fi
}

# clear input folders
rm ./mAP/input/ground-truth/*
rm ./mAP/input/detection-results/*

# copy ground truth
cp ../object-detection/${TRUTHDIR}/*.txt ./mAP/input/ground-truth/

print_mAP "random/0/memcopy/uniform"
print_mAP "adaptive/0/memcopy/uniform"
print_mAP "adaptive/1/memcopy/uniform"
print_mAP "adaptive/1/static/uniform"
print_mAP "adaptive/1/dynamic/uniform"
print_mAP "adaptive/1/dynamic/minsum"
print_mAP "adaptive/1/dynamic/minmax"
