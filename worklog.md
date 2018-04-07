# Workflow

1. Run [split_libraries.pbs](./scripts/split_libraries.pbs)
  * __Time:__ 72m55.923s
  * __Logs:__ ~/18/split_data/split_library_log.txt
  * __Output directory:__ ~/18/split_data/

1. Run [pick_OTU.pbs](./scripts/pick_OTU.pbs)
  * __Time:__ 9m3.530s
  * __Logs:__ ~/18/closed_otus/log_20180407190923.txt
  * __Output directory:__ ~/18/closed_otus/

1. Run [pick_rep_set.pbs](./scripts/pick_rep_set.pbs)
  * __Time:__ 5m54.436s
  * __Logs:__ ~/18/pick_rep_set/rep_set.log
  * __Output directory:__ ~/18/pick_rep_set/

1. Run [asign_taxonomy.pbs](./scripts/assign_taxonomy.pbs)
  * __Time:__ 3m14.096s
  * __Logs:__ None
  * __Output directory:__ ~/18/assigned_taxonomy/

