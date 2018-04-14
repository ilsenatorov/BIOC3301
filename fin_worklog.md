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
  * Time: 887.30
  * Output: ~/18/core_div
