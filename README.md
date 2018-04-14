# Repo for working on the Cirrus HPC

## Important branches info!

Branch [master](https://github.com/ilsenatorov/cirrus_BIOC3301/tree/master) has all the data, including what was created outside cirrus, while branch [cirr_local](https://github.com/ilsenatorov/cirrus_BIOC3301/tree/cirr_local) can be cloned directly to the machine, since it only contains scripts that are run on the HPC. To clone only one branch, type:

`git clone -b cirr_local https://github.com/ilsenatorov/cirrus_BIOC3301.git`, which will create a folder with all the Cirrus scripts inside the folder. Remember that the scripts need to be run from home directory, so copy them using `cp <script to use> ~`

Another option is to fetch, using these commands in the home directory:
```
cd ~
git init
git add remote origin https://github.com/ilsenatorov/cirrus_BIOC3301.git
git pull origin cirr_local
```
This will put the scripts into the home directory on Cirrus

## Commands available

### benchmark_script.sh

runs a script with diffeent number of cores. Takes the location of the script to test as first positional argument - `./benchmark_script.sh <script to benchmark>`. Make sure that script to benchmark is using a truncated dataset, for example __seqs_500k.fna__ instead of __seqs.fna__.

### get_logs.sh

Collects all the logs created by __benchmark_script.sh__ and creates a logfile from them. Takes the names of logfiles without the extensions but with the dot, for example `./get_logs.sh my_benchmarking_logs.` 

__Won't work without the dot at the end!__

### filter_barcode.py

filters the seqs.fna or any other file in that format to only have samples from one team/with one barcode. Run with `./filter_barcode.py -i <location of input fna file> -o <output file> -b <barcode number, for 515rcbc20 it will be 20>`. For more info run `./filter_barcode.py --help`.

## Scripts folder

Has the scripts I used for working with the dataset, the ones that start with and underscore _ are unfinished. Has a useful [template](./scripts/template) which has the parts of script that should be present in all PBS scripts.
