# Workflow

## Introduction
This file briefly describes what scripts were run in what order. Some results were used in multiple sequences.

### First run with Greengenes

1. Run [validate_mapping.pbs](./scripts/validate_mapping.pbs)
  * __Time:__ 31.02s
  * __Output directory:__ ~/18/map_validation/
1. Run [split_libraries.pbs](./scripts/split_libraries.pbs)
  * __Time:__ 72m55.923s
  * __Output directory:__ ~/18/split_data/
1. Run [pick_OTU.pbs](./scripts/pick_OTU.pbs)
  * __Time:__ 9m3.530s
  * __Output directory:__ ~/18/closed_otus/
1. Run [pick_rep_set.pbs](./scripts/pick_rep_set.pbs)
  * __Time:__ 5m54.436s
  * __Output directory:__ ~/18/pick_rep_set/
1. Run [asign_taxonomy.pbs](./scripts/assign_taxonomy.pbs)
  * __Time:__ 3m14.096s
  * __Output directory:__ ~/18/assigned_taxonomy/
1. Run [filter_alignment.pbs](./scripts/filter_alignment.pbs)
  * __Time:__ 88.42s
  * __Output directory:__ ~/18/filter_align
1. Run [make_phylogen.pbs](./scripts/make_phylogen.pbs)
  * __Time:__ 166.25s
  * __Output directory:__ ~/18/my_tree/
1. Run [core_div_analyses.pbs](./scripts/core_div_analyses.pbs)
  * __Time:__ 496.71s
  * __Output directory:__ ~/18/core_div
1. Run [make_phylogen_clearcut.pbs](./scripts/make_phylogen_clearcut.pbs)
  * __Time:__ 299.85s
  * __Output directory:__ ~/18/tree/

### Silva run

1. Run [validate_mapping.pbs](./scripts/validate_mapping.pbs)
  * __Time:__ 31.02s
  * __Output directory:__ ~/18/map_validation/
1. Run [split_libraries.pbs](./scripts/split_libraries.pbs)
  * __Time:__ 72m55.923s
  * __Output directory:__ ~/18/split_data/
1. Run [pick_silva_otus.pbs](./scripts/pick_silva_OTU.pbs)
  * __Time:__ 678.98s
  * __Output directory:__ ~/18/silva_otus
1. Run [pick_rep_silva.pbs](./scripts/pick_rep_silva.pbs)
  * __Time:__ 172.95s
  * __Output directory:__ ~/18/silva_otus
1. Run [ident_chim.pbs](./scripts/ident_chim.pbs)
  * __Time:__
  * __Output directory:__
