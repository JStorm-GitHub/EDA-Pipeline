clock_opt -clock_trees {ideal_clock1}

### Reports 
report_placement_utilization > cts/reports/${file_name}_cts_util.rpt
report_qor_snapshot > cts/reports/${file_name}_cts_qor_snapshot.rpt
report_qor > cts/reports/${file_name}_cts_qor.rpt
report_power > cts/reports/${file_name}_cts_power.rpt


report_timing -max_paths 20 -delay max > cts/reports/${file_name}_cts.setup.rpt
report_timing -max_paths 20 -delay min > cts/reports/${file_name}_cts.hold.rpt
