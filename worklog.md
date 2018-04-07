# Workflow

1. Run [split_libraries.pbs](./scripts/split_libraries.pbs)
  * __Time:__ 72m55.923s
  * __Logs:__ ~/18/split_data/split_library_log.txt
  * __Output directory:__ ~/18/split_data/
2. Run [pick_OTU.pbs](./scripts/pick_OTU.pbs)
  * __Time:__ 9m3.530s
  * __Logs:__ ~/18/closed_otus/log_20180407190923.txt
  * __Output directory:__ ~/18/closed_otus/
3. Run [pick_rep_set.pbs](./scripts/pick_rep_set.pbs)
  * __Time:__ 5m54.436s
  * __Logs:__ ~/18/pick_rep_set/rep_set.log
  * __Output directory:__ ~/18/pick_rep_set/
4. Run [asign_taxonomy.pbs](./scripts/assign_taxonomy.pbs)
  * __Time:__ 3m14.096s
  * __Logs:__ None
  * __Output directory:__ ~/18/assigned_taxonomy/
5. Run [filter_alignment.pbs](./scripts/filter_alignment.pbs)
  * __Time:__ 88.42s
  * __Logs:__ None
  * __Output directory:__ ~/18/filter_align
6. Run [make_phylogen.pbs](./scripts/make_phylogen.pbs)
  * __Time:__ 166.25s
  * __Logs:__ ~/18/tree/tree.log
  * __Output directory:__ ~/18/my_tree/
