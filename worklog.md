# Workflow

1. Run [validate_mapping.pbs](./scripts/validate_mapping.pbs)
__Time:__ 31.02s
__Logs:__ ~/18/map_validation/map_incomplete.tsv.log
__Output directory:__ ~/18/map_validation/
1. Run [split_libraries.pbs](./scripts/split_libraries.pbs)
__Time:__ 72m55.923s
__Logs:__ ~/18/split_data/split_library_log.txt
__Output directory:__ ~/18/split_data/
1. Run [pick_OTU.pbs](./scripts/pick_OTU.pbs)
__Time:__ 9m3.530s
__Logs:__ ~/18/closed_otus/log_20180407190923.txt
__Output directory:__ ~/18/closed_otus/
1. Run [pick_rep_set.pbs](./scripts/pick_rep_set.pbs)
__Time:__ 5m54.436s
__Logs:__ ~/18/pick_rep_set/rep_set.log
__Output directory:__ ~/18/pick_rep_set/
1. Run [asign_taxonomy.pbs](./scripts/assign_taxonomy.pbs)
__Time:__ 3m14.096s
__Logs:__ None
__Output directory:__ ~/18/assigned_taxonomy/
1. Run [filter_alignment.pbs](./scripts/filter_alignment.pbs)
__Time:__ 88.42s
__Logs:__ None
__Output directory:__ ~/18/filter_align
1. Run [make_phylogen.pbs](./scripts/make_phylogen.pbs)
__Time:__ 166.25s
__Logs:__ ~/18/tree/tree.log
__Output directory:__ ~/18/my_tree/
1. Run [core_div_analyses.pbs](./scripts/core_div_analyses.pbs)
__Time:__ 496.71s
__Logs:__ ~/core_div/log_20180408110240.txt
__Output directory:__ ~/18/core_div
1. Run [make_phylogen_clearcut.pbs](./scripts/make_phylogen_clearcut.pbs)
__Time:__ 299.85s
__Logs:__ None
__Output directory:__ ~/18/tree/
