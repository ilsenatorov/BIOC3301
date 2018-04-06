#/bin/bash

for err in $1e*; do
  echo $err
  out=$(echo $err | rev | sed 's/e/o/' | rev)
  echo $out
  grep "Number of cores" $out >> times.log
  grep "real" $err >> times.log
done
cat times.log
