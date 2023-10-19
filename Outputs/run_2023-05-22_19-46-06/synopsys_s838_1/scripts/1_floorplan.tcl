create_floorplan -core_utilization 0.6 \
    -left_io2core 5 -bottom_io2core 5 -right_io2core 5 -top_io2core 5
derive_pg_connection -power_net VDD_ -ground_net VSS
derive_pg_connection -power_net VDD_ -ground_net VSS -tie

##Create VSS ring
create_rectangular_rings  -nets  {VSS}  \
    -left_offset 0.5  -left_segment_layer M6 -left_segment_width 1.0 -extend_ll -extend_lh \
    -right_offset 0.5 -right_segment_layer M6 -right_segment_width 1.0 -extend_rl -extend_rh \
    -bottom_offset 0.5  -bottom_segment_layer  M7 -bottom_segment_width 1.0 -extend_bl -extend_bh \
    -top_offset 0.5 -top_segment_layer M7 -top_segment_width 1.0 -extend_tl -extend_th
    
## Create VDD Ring
create_rectangular_rings  -nets  {VDD_}  \
    -left_offset 1.8  -left_segment_layer M6 -left_segment_width 1.0 -extend_ll -extend_lh \
    -right_offset 1.8 -right_segment_layer M6 -right_segment_width 1.0 -extend_rl -extend_rh \
    -bottom_offset 1.8  -bottom_segment_layer M7 -bottom_segment_width 1.0 -extend_bl -extend_bh \
    -top_offset 1.8 -top_segment_layer M7 -top_segment_width 1.0 -extend_tl -extend_th

## Creates Power Strap 
create_power_strap -nets { VDD_ } -layer M6 -direction vertical -width 3  
create_power_strap -nets { VSS } -layer M6 -direction vertical  -width 3

report_qor > floorplan/reports/${file_name}_floorplan_qor.rpt
report_power > floorplan/reports/${file_name}_floorplan_power.rpt
