#!/bin/bash

if [ "$#" -ne 1 ]; then
   echo "usage: $0 [net]"
   exit 1
fi

NET=$1
DEFAULT_SEED=4716771

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

echo -e "queue10 (q_10,rate_50,tile_3_3)  "
sweep_lat 0 9 50 ${DEFAULT_SEED} der_and_stdev 10
exit 1

# tiles_3_2
echo -e "tile_3_2  "
sweep_lat 1 6 50 ${DEFAULT_SEED} der_and_stdev 5

# tiles_4_2
echo -e "tile_4_2  "
sweep_lat 1 8 50 ${DEFAULT_SEED} der_and_stdev 5

# seed_B
echo -e "seed_B  "
sweep_lat 1 9 50 12345678 der_and_stdev 5

# seed_C
echo -e "seed_C  "
sweep_lat 1 9 50 87654321 der_and_stdev 5

# seed_D
echo -e "seed_D  "
sweep_lat 1 9 50 56781234 der_and_stdev 5

# seed_E
echo -e "seed_E  "
sweep_lat 1 9 50 43218765 der_and_stdev 5

# baseline
echo -e "baseline  "
sweep_lat 0 9 50 ${DEFAULT_SEED} der_and_stdev 5

# stdev
echo -e "stdev  "
sweep_lat 0 9 50 ${DEFAULT_SEED} stdev 5

# frequency_100
echo -e "frequency_100  "
sweep_lat 0 9 100 ${DEFAULT_SEED} der_and_stdev 5

# frequency_25
echo -e "frequency_25  "
sweep_lat 0 9 25 ${DEFAULT_SEED} der_and_stdev 5
