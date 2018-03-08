#!/bin/bash --login
for f in {1,2,4,8,16,24,32}; do
  qsub -v "cores=$f" parallel.cbs
done
