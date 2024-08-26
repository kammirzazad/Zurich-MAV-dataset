#!/bin/bash

BASELINE_RATE=50
BASELINE_SEED=4716771
BASELINE_TILES=$((3*3))
BASELINE_QUEUESIZE=5
BASELINE_LAYERGROUPS=7

RESDIR="../../DREML-data/simulator/IMG_SEG"
TRUTHDIR="../image-segmentation/resized/512/1-fps-200/"

sweep_lat() {
   SETTING=$1
   METRIC=$2
   QUEUESIZE=$3
   GRIDSIZE=$4
   UPDATEFREQ=$5
   LAYERGROUPS=$6
   SEED=$7
   declare -a LATS=("0.1" "0.2" "0.3" "0.4" "0.45" "0.5") # "0.55" "0.6") # "0.7" "0.8")
   echo -e "${SETTING}"
   for LATENCY in "${LATS[@]}"
   do
      echo -e -n "${LATENCY}:\t"
      DIR="${RESDIR}/${METRIC}/${QUEUESIZE}/${GRIDSIZE}/${UPDATEFREQ}/${LAYERGROUPS}/tcp/${SEED}/${SETTING}/${LATENCY}/"
      python3 iseg_coeff.py ${DIR} ${TRUTHDIR} ${QUEUESIZE}
   done
}

sweep_opts() {
   GRIDSIZE=$1
   UPDATEFREQ=$2
   SEED=$3
   METRIC=$4
   QUEUESIZE=$5
   sweep_lat "random/0/memcopy/uniform"   ${METRIC} ${QUEUESIZE} ${GRIDSIZE} ${UPDATEFREQ} ${BASELINE_LAYERGROUPS} ${SEED}
   sweep_lat "adaptive/0/memcopy/uniform" ${METRIC} ${QUEUESIZE} ${GRIDSIZE} ${UPDATEFREQ} ${BASELINE_LAYERGROUPS} ${SEED}
   sweep_lat "adaptive/1/memcopy/uniform" ${METRIC} ${QUEUESIZE} ${GRIDSIZE} ${UPDATEFREQ} ${BASELINE_LAYERGROUPS} ${SEED}
   sweep_lat "adaptive/1/static/uniform"  ${METRIC} ${QUEUESIZE} ${GRIDSIZE} ${UPDATEFREQ} ${BASELINE_LAYERGROUPS} ${SEED}
   sweep_lat "adaptive/1/dynamic/uniform" ${METRIC} ${QUEUESIZE} ${GRIDSIZE} ${UPDATEFREQ} ${BASELINE_LAYERGROUPS} ${SEED}
   sweep_lat "adaptive/1/dynamic/minmax"  ${METRIC} ${QUEUESIZE} ${GRIDSIZE} ${UPDATEFREQ} ${BASELINE_LAYERGROUPS} ${SEED}
}

# baseline
echo -e "baseline"
sweep_opts ${BASELINE_TILES} ${BASELINE_RATE} ${BASELINE_SEED} der_and_stdev ${BASELINE_QUEUESIZE}

# frequency_100
echo -e "frequency_100  "
sweep_opts ${BASELINE_TILES} 100 ${BASELINE_SEED} der_and_stdev ${BASELINE_QUEUESIZE}

# frequency_25
echo -e "frequency_25  "
sweep_opts ${BASELINE_TILES} 25  ${BASELINE_SEED} der_and_stdev ${BASELINE_QUEUESIZE}

# queue_2
echo -e "queue_2  "
sweep_opts ${BASELINE_TILES} ${BASELINE_RATE} ${BASELINE_SEED} der_and_stdev 2

# queue_10
echo -e "queue_10  "
sweep_opts ${BASELINE_TILES} ${BASELINE_RATE} ${BASELINE_SEED} der_and_stdev 10
