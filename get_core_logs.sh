#!/bin/bash --login

### SCRIPT to extract the times it took to run the becnhmark script

### puts all the important info into the times.log file in the same directory 



for err in _2017_cr_nojoin_no_golay_parallel.e*; do
  out=$(echo $err | rev | sed 's/e/o/' | rev)
  grep "Number of cores" $out >> times.log
  grep "real" $err >> times.log
done
