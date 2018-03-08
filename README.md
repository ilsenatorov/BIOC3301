## Repo for working on the Cirrus HPC

### How to use the scripts

run `bash <command_name>` from the terminal

### Commands available

#### _get_core_logs.sh_

Extracts the real run times from all the logs in the directory, together with the number of cores, puts them all in the times.log file in the current dir
Output looks like this:

```
Number of cores chosen is 1
real    4m2.500s
Number of cores chosen is 2
real    2m17.073s                                                                                                                   
Number of cores chosen is 4                                                                                                         
real    1m24.652s                                                                                                                   
Number of cores chosen is 8                                                                                                         
real    0m57.940s                                                                                                                   
Number of cores chosen is 16                                                                                                        
real    0m48.751s                                                                                                                   
Number of cores chosen is 24                                                                                                        
real    0m48.441s                                                                                                                   
Number of cores chosen is 32                                                                                                        
real    0m38.918s        
```

which can then be used to calculate efficiency

#### run_parall_benchm.sh

Runs the benchmarking script (parallel.cbs) with 1,2,4,8,16,24 and 32 cores

#### parallel.cbs 

Measures time it took to run the qiime script pick_closed_reference_otus.py, takes the number of cores as the first positional argument.
_Example:_ `qsub -v "cores=4" parallel.cbs` will run the code with 4 cores

#### Useful commands
* `rm _2017_cr_nojoin_no_golay_parallel.*` will remove all files that are created by benchmarking script (that start with _2017_cr_ etc)
* `rm -r otus*` will remove all the otus directories created by the script _make sure they don't have any important info!_
