###########################################################################
### Initialize
###########################################################################

set search_path "$search_path /mnt/class_data/ecec574-w2019/PDKs/SAED32nm/lib/stdcell_rvt/db_ccs
../src/ "
set target_library "saed32rvt_ss0p95v25c.db"
set link_library "* $target_library"
set techfile "/mnt/class_data/ecec574-w2019/PDKs/SAED32nm/tech/milkyway/saed32nm_1p9m_mw.tf"
set ref_lib "/mnt/class_data/ecec574-w2019/PDKs/SAED32nm/lib/stdcell_rvt/milkyway/saed32nm_rvt_1p9m"
set lib_name "${file_name}"
set mw_logic0_net VSS
set mw_logic1_net VDD_
create_mw_lib $lib_name.mw -technology $techfile -mw_reference_library $ref_lib 
open_mw_lib $lib_name.mw

set design_data logical_synthesis/outputs/${file_name}.ddc
set cell_name "${file_name}"
import_designs $design_data -format ddc -top $cell_name

set libdir "/mnt/class_data/ecec574-w2019/PDKs/SAED32nm/tech/star_rcxt"
set tlupmax "$libdir/saed32nm_1p9m_Cmax.tluplus"
set tlunom "$libdir/saed32nm_1p9m_nominal.tluplus"
set tlupmin "$libdir/saed32nm_1p9m_Cmin.tluplus"
set tech2itf "$libdir/saed32nm_tf_itf_tluplus.map"
set_tlu_plus_files -max_tluplus $tlunom -tech2itf_map $tech2itf

read_verilog logical_synthesis/outputs/${file_name}.v
uniquify_fp_mw_cel
link
read_sdc logical_synthesis/outputs/${file_name}.sdc

###########################################################################
### Floorplanning
###########################################################################

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

report_fp_placement_strategy > floorplan/reports/${file_name}_floorplan_strategy.rpt


###########################################################################
### Placement
###########################################################################

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
report_timing -delay max -max_paths 20 > placed/reports/${file_name}_place.setup.rpt
report_timing -delay min -max_paths 20 > placed/reports/${file_name}_place.hold.rpt

###########################################################################
### Clock Tree Synthesis
###########################################################################

clock_opt -clock_trees {ideal_clock1}

### Reports 
report_placement_utilization > cts/reports/${file_name}_cts_util.rpt
report_qor_snapshot > cts/reports/${file_name}_cts_qor_snapshot.rpt
report_qor > cts/reports/${file_name}_cts_qor.rpt
report_timing -max_paths 20 -delay max > cts/reports/${file_name}_cts.setup.rpt
report_timing -max_paths 20 -delay min > cts/reports/${file_name}_cts.hold.rpt

###########################################################################
### Routing
###########################################################################

set_route_mode_options -zroute true
route_opt -effort low 

### Reports 
report_placement_utilization > routed/reports/${file_name}_route_util.rpt
report_qor_snapshot > routed/reports/${file_name}_route_qor_snapshot.rpt
report_qor > routed/reports/${file_name}_route_qor.rpt
report_timing -max_paths 50 -delay max > routed/reports/${file_name}_route.setup.rpt
report_timing -max_paths 50 -delay min > routed/reports/${file_name}_route.hold.rpt

###########################################################################
### Extraction
###########################################################################

extract_rc  -coupling_cap  -routed_nets_only  -incremental

## write parasitic to a file for delay calculations tools (e.g PrimeTime).
write_parasitics -output extracted/outputs/${file_name}_extracted.spef -format SPEF

## Write Standard Delay Format (SDF) back-annotation file
write_sdf extracted/outputs/${file_name}_extracted.sdf

## Write out a script in Synopsys Design Constraints format
write_sdc extracted/outputs/${file_name}_extracted.sdc -version 2.0

## Write out a hierarchical Verilog file for the current design, extracted from layout
write_verilog extracted/outputs/${file_name}_extracted.v

##Save the cel and report timing
report_timing -max_paths 50 -delay max > extracted/reports/${file_name}_extracted.setup.rpt
report_timing -max_paths 50 -delay min > extracted/reports/${file_name}_extracted.hold.rpt

save_mw_cel -as ${file_name}_extracted

###########################################################################
### Generate relevant final reports
###########################################################################

report_qor > final/reports/${file_name}_final_qor.rpt
report_timing > final/reports/${file_name}_final_timing.rpt
report_power > final/reports/${file_name}_final_power.rpt
report_cell > final/reports/${file_name}_final_cells.rpt
report_clock_tree -summary > final/reports/${file_name}_final_ct.rpt

exit
