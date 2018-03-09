#!/bin/bash --login

### runs the benchmarking script for different number of cores

for f in {1,2,4,8,16,24,32}; do
  sed -i -e "s/.*PBS -l select=1:ncpus=.*/\#PBS -l select=1:ncpus=$((f*2))/" parallel.pbs
  qsub -v "cores=$f" parallel.pbs
done


