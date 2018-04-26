# Workflow

### Silva

1. Download the data into ~/18/raw_data
1. Run [map_validation.pbs](./fin_scripts/map_validation.pbs)
  * Time: 5.37s
  * Output: ~/18/map_validation
1. Copy and rename mapping file `cp ~/18/map_validation/map.tsv_corrected.txt ~/18/map.tsv`
1. Run [join_ends.pbs](./fin_scripts/join_ends.pbs)
  * Time: 2411.27s
  * Output: ~/18/joined
1. Run [split_lib.pbs](./fin_scripts/split_lib.pbs)
  * Time: 2122.14s
  * Output: ~/18/split_data
1. Run [pick_OTU_silva.pbs](./fin_scripts/pick_OTU_silva.pbs)
  * Time: 430.24s
  * Output: ~/18/silva_otus
1. Run [corediv.pbs](./fin_scripts/corediv.pbs)
  * Time: 887.30s
  * Output: ~/18/core_div
1. Run [align.pbs](./fin_scripts/align.pbs)
  * Time: 2309.78s
  * Output: ~/18/aligned/
1. Run [filter_alignment.pbs](./fin_scripts/filter_alignment.pbs)
  * Time: 288.83s
  * Output: ~/18/filtered_aligned/


### [Sourcetracker 2](https://github.com/biota/sourcetracker2)
1. Install sourcetracker 2, creating the st2 environment in the process
1. Run [batch_sourcetrack.pbs](./fin_scripts/batch_sourcetrack.pbs)
  * __NB:__ this is a batch script, so it runs 4 script in one go. Look at the code for more info.
    * Merging OTU tables
    * 1617.08s
    * Filter table according to map
    * 111.72s
    * Filter OTUs present in less than 500
    * 97.69s
    * Filter samples less than 1300
    * 56.28s
  * Output: ~/sourcetracker
1. Run [run_sourcetrack.pbs](./fin_scripts/run_sourcetrack.pbs). __NB:__ uses st2 environment
  * Time: 2040.81s
  * Output: ~/sourcetracker/tracked
