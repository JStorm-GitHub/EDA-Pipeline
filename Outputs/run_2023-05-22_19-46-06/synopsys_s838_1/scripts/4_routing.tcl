set_route_mode_options -zroute true
route_opt -effort low 

### Reports 
report_placement_utilization > routed/reports/${file_name}_route_util.rpt
report_qor_snapshot > routed/reports/${file_name}_route_qor_snapshot.rpt
report_qor > routed/reports/${file_name}_route_qor.rpt
report_power > routed/reports/${file_name}_route_power.rpt


report_timing -max_paths 50 -delay max > routed/reports/${file_name}_route.setup.rpt
report_timing -max_paths 50 -delay min > routed/reports/${file_name}_route.hold.rpt
