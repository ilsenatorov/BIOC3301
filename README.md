# Repo for working on the Cirrus HPC

## How to use the scripts

run `bash <command_name>` from the terminal

## Commands available

### benchmark_script.sh

runs a script with diffeent number of cores. Takes the location of the script to test as first positional argument - `./benchmark_script.sh <script to benchmark>`. Make sure that <script to benchmark> is using a truncated dataset, for example __seqs_500k.fna__ instead of __seqs.fna__. 

### get_logs.sh

Collects all the logs created by __benchmark_script.sh__ and creates a logfile from them. Takes the names of logfiles without the extensions but with the dot, for example `./get_logs.sh my_benchmarking_logs.`. __Won't work without the dot at the end!__

## Scripts folder

Has the scripts I used for working with the dataset, the ones that start with and underscore _ are unfinished. Has a useful pbs_template which has the parts of script that should be present in all PBS scripts.
