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
1. Run [filter_sample.pbs](./fin_scripts/filter_sample.pbs) with `sample=515rcbc20`
  * Time: 519.93
  * Output: ~/18/filtered_otus/515rcbc20/

### Sourcetrack
1. Download the EMP data [1](ftp://ftp.microbio.me/emp/release1/otu_tables/closed_ref_silva/emp_cr_silva_16S_123.qc_filtered.biom) [2](ftp://ftp.microbio.me/emp/release1/mapping_files/emp_qiime_mapping_qc_filtered.tsv)
1. Parse the EMP mapping file using [this script](./fin_scripts/parse_mapping.py)
1. Manually add the original mapping file to the EMP one, adding __sink__ in the SourceSink column
1. Merge otu tables using [merge_otu.pbs](./fin_scripts/merge_otu.pbs)
  * Time: 2302.89s
1. Filter the otu table so it contains only otus with  7+ samples usin [filter_sample.pbs](./fin_scripts/filter_sample.pbs)
1. [Convert the biom table to tsv](./fin_scripts/convert_tsv.pbs)
1. Run [track_source.pbs](./fin_scripts/track_source.pbs)
