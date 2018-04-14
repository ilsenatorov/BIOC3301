#/bin/bash

for err in $1e*; do
  echo $err
  out=$(echo $err | rev | sed 's/e/o/' | rev)
  echo $out
  grep "Number of cores" $out >> benchmarking_times.log
  grep "real" $err >> benchmarking_times.log
done
cat benchmarking_times.log
