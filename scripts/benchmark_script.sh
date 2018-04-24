#!/bin/bash --login

### runs the benchmarking script for different number of cores
# to use call it with the benchmarking script as the first positional argument

for f in {1,2,4,8,16,24,32}; do
  sed -i -e "s/.*PBS -l select=1:ncpus=.*/\#PBS -l select=1:ncpus=$((f*2))/" $1
  qsub -v "cores=$f" $1
done
