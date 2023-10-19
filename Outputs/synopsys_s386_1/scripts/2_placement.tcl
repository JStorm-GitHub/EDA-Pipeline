set_buffer_opt_strategy -effort low
set_tlu_plus_files \
    -max_tluplus /mnt/class_data/ecec574-w2019/PDKs/SAED32nm/tech/star_rcxt/saed32nm_1p9m_Cmax.tluplus \
    -min_tluplus /mnt/class_data/ecec574-w2019/PDKs/SAED32nm/tech/star_rcxt/saed32nm_1p9m_Cmin.tluplus \
    -tech2itf_map /mnt/class_data/ecec574-w2019/PDKs/SAED32nm/tech/star_rcxt/saed32nm_tf_itf_tluplus.map
place_opt -congestion

### Reports 

report_placement_utilization > placed/reports/${file_name}_place_util.rpt
report_qor_snapshot > placed/reports/${file_name}_place_qor_snapshot.rpt
report_qor > placed/reports/${file_name}_place_qor.rpt
report_power > placed/reports/${file_name}_place_power.rpt

report_timing -delay max -max_paths 20 > placed/reports/${file_name}_place.setup.rpt
report_timing -delay min -max_paths 20 > placed/reports/${file_name}_place.hold.rpt
