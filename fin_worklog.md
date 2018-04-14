# Workflow

### Silva

1. Download the data into ~/18/raw_data
1. Run [map_validation.pbs](./fin_scripts/map_validation.pbs)
  * Time: 5.37s
  * Output: ~/18/map_validation
1. Copy and rename mapping file `cp ~/18/map_validation/map.tsv_corrected.txt ~/18/map.tsv`
1. Run [join_ends.pbs](./fin_scripts/join_ends.pbs)
  * Time: 
  * Output: ~/18/joined

