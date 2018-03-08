#!/bin/bash --login
#rm times.log || echo "no logfile"
for err in _2017_cr_nojoin_no_golay_parallel.e*; do
  out=$(echo $err | rev | sed 's/e/o/' | rev)
  grep "Number of cores" $out >> times.log
  grep "real" $err >> times.log
done
