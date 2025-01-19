#!/bin/bash

if [ "$#" -ne 1 ]; then
   echo "usage: $0 [net]"
   exit 1
fi

NET=$1
BASELINE_RATE=50
BASELINE_SEED=4716771
BASELINE_TILES=$((3*3))
BASELINE_QUEUESIZE=5

if [ "$NET" = "YOLOv2" ]; then
   LAYERGROUPS=2
elif [ "$NET" = "YOLOv3" ]; then
   LAYERGROUPS=5
else
   echo Unknown network ${NET}
   exit 1
fi

sweep_lat() {
   FULLOPTONLY=$1
   GRIDSIZE=$2
   UPDATEFREQ=$3
   SEED=$4
   METRIC=$5
   QUEUESIZE=$6
   declare -a LATS=("0.1" "0.2" "0.3" "0.4" "0.45" "0.5") # "0.55" "0.6") # "0.7" "0.8")
   for LAT in "${LATS[@]}"
   do
      #[net] [latency <1.0] [gridSize] [updateFreq] [layerGroups] [seed] [metric] [fullOptOnly]"
      echo -e -n "$LAT: "
      ./mAP_all.sh ${NET} ${LAT} ${GRIDSIZE} ${UPDATEFREQ} ${LAYERGROUPS} ${SEED} ${METRIC} ${FULLOPTONLY} ${QUEUESIZE}
   done
}

#echo -e "tile_4_2 (q_5,rate_50,tile_4_2)  "
#sweep_lat 0 8 ${BASELINE_RATE} ${BASELINE_SEED} der_and_stdev ${BASELINE_QUEUESIZE}
#exit 1

# tiles_3_2
#echo -e "tile_3_2  "
#sweep_lat 1 6 ${BASELINE_RATE} ${BASELINE_SEED} der_and_stdev ${BASELINE_QUEUESIZE}

# tiles_4_2
#echo -e "tile_4_2  "
#sweep_lat 1 8 ${BASELINE_RATE} ${DEFAULT_SEED} der_and_stdev ${BASELINE_QUEUESIZE}

# seed_B
#echo -e "seed_B  "
#sweep_lat 1 ${BASELINE_TILES} ${BASELINE_RATE} 12345678 der_and_stdev ${BASELINE_QUEUESIZE}

# seed_C
#echo -e "seed_C  "
#sweep_lat 1 ${BASELINE_TILES} ${BASELINE_RATE} 87654321 der_and_stdev ${BASELINE_QUEUESIZE}

# seed_D
#echo -e "seed_D  "
#sweep_lat 1 ${BASELINE_TILES} ${BASELINE_RATE} 56781234 der_and_stdev ${BASELINE_QUEUESIZE}

# seed_E
#echo -e "seed_E  "
#sweep_lat 1 ${BASELINE_TILES} ${BASELINE_RATE} 43218765 der_and_stdev ${BASELINE_QUEUESIZE}

# baseline
echo -e "baseline  "
sweep_lat 0 ${BASELINE_TILES} ${BASELINE_RATE} ${BASELINE_SEED} der_and_stdev ${BASELINE_QUEUESIZE}

# stdev
#echo -e "stdev  "
#sweep_lat 0 ${BASELINE_TILES} ${BASELINE_RATE} ${BASELINE_SEED} stdev ${BASELINE_QUEUESIZE}

# frequency_100
echo -e "frequency_100  "
sweep_lat 0 ${BASELINE_TILES} 100 ${BASELINE_SEED} der_and_stdev ${BASELINE_QUEUESIZE}

# frequency_25
echo -e "frequency_25  "
sweep_lat 0 ${BASELINE_TILES} 25  ${BASELINE_SEED} der_and_stdev ${BASELINE_QUEUESIZE}

# queue_2
echo -e "queue_2  "
sweep_lat 0 ${BASELINE_TILES} ${BASELINE_RATE} ${BASELINE_SEED} der_and_stdev 2

# queue_10
echo -e "queue_10  "
sweep_lat 0 ${BASELINE_TILES} ${BASELINE_RATE} ${BASELINE_SEED} der_and_stdev 10

