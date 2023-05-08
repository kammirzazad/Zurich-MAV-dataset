#!/bin/bash

if [ "$#" -ne 4 ]; then
    echo "usage: $0 [latency <1.0] [gridSize] [updateFreq] [layerGroups]"
    exit 1
fi

LATENCY=$1
GRIDSIZE=$2
UPDATEFREQ=$3
LAYERGROUPS=$4
#SEED="4716771"
SEED="12345678"
#SEED="87654321"
#SEED="56781234"
#SEED="43218765"
PROTOCOL="tcp"
RESDIR="../../DREML-data/simulator/IMG_SEG"
TRUTHDIR="../Zurich-MAV-dataset/image-segmentation/resized/512/30-fps/"

print_coeff () {
   echo -e -n "$1   \t"
   DIR=$RESDIR/$GRIDSIZE/$UPDATEFREQ/$LAYERGROUPS/$PROTOCOL/$SEED/$1/$LATENCY/
   python3 iseg_coeff.py $DIR $TRUTHDIR
}

print_coeff "random/0/memcopy/uniform"
print_coeff "adaptive/0/memcopy/uniform"
print_coeff "adaptive/1/memcopy/uniform"
#print_coeff "adaptive/1/memcopy/minsum"
print_coeff "adaptive/1/memcopy/minmax"
