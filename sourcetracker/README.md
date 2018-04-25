## [Sourcetracker2](https://github.com/biota/sourcetracker2) workflow

1. Download the [biom table](ftp://ftp.microbio.me/emp/release1/otu_tables/closed_ref_silva/emp_cr_silva_16S_123.qc_filtered.biom) and the [mapping file](ftp://ftp.microbio.me/emp/release1/mapping_files/emp_qiime_mapping_qc_filtered.tsv) from EMP release 1
1. Parse through the EMP mapping file to only select soil samples using [parse_mapping.py](../scripts/parse_mapping.py)
1. Merge the EMP mapping file and experiment's mapping file, adding the SourceSink column and labeling all of the EMP data as Source and all experimental data as sink, while also renaming the column with source of data _(park, tundra, permafrost etc)_ to "Env".
1. Install sourcetracker2, following the [guideline](https://github.com/biota/sourcetracker2) provided.
1. Launch [batch_sourcetrack.pbs](../scripts/batch_sourcetrack.pbs)
  * __NB:__ this is a batch script, so it runs 4 script in one go. Look at the code for more info.
    * Merging OTU tables
    * 1617.08s
    * Filter table according to map
    * 111.72s
    * Filter OTUs present in less than 500
    * 97.69s
    * Filter samples less than 1300
    * 56.28s
1. Run [run_sourcetrack.pbs](../scripts/run_sourcetrack.pbs). __NB:__ uses st2 environment
  * Time: 2040.81s
1. This produces the 2 files used for downstream analysis presented here - [percentage table](./mixing_proportions.txt) and [standard deviation table](./mixing_proportions_stds.txt)
