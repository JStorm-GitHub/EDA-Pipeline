###### DC Synthesis Script #######

## Give the path to the verilog files and define the WORK directory




lappend search_path [pwd]/src
define_design_lib WORK -path work


## Define the library location
set link_library [ list /mnt/class_data/ecec574-w2019/PDKs/SAED32nm/lib/stdcell_rvt/db_ccs/saed32rvt_ss0p95v125c.db /mnt/class_data/ecec574-w2019/PDKs/SAED32nm/lib/stdcell_rvt/db_ccs/saed32rvt_ss0p95v25c.db /mnt/class_data/ecec574-w2019/PDKs/SAED32nm/lib/stdcell_rvt/db_ccs/saed32rvt_ss0p95vn40c.db ]
set target_library [ list /mnt/class_data/ecec574-w2019/PDKs/SAED32nm/lib/stdcell_rvt/db_ccs/saed32rvt_ss0p95v25c.db ]


## read the verilog files
analyze -library WORK -format verilog [list dff.v "${file_name}.v"]
elaborate -architecture verilog -library WORK $file_name
current_design $file_name
link


## Check if design is consistent
check_design  > logical_synthesis/reports/synth_check_design.rpt


## Create Constraints

create_clock CK -name ideal_clock1 -period 2
set_input_delay $in_delay [ remove_from_collection [ all_inputs ] CK ] -clock ideal_clock1
set_output_delay $out_delay [ all_outputs ] -clock ideal_clock1
set_load $s_load [ all_outputs ]
set_max_area 0

# Set Clock Constraints
set_clock_latency 0.4 [ get_clocks ideal_clock1 ]
set_clock_uncertainty $s_clk_uncert [ get_clocks ideal_clock1 ]
set_clock_transition 0.1 ideal_clock1


## Compilation
compile -area_effort $c_area_effort -map_effort $c_map_effort



## Below commands report area , cell, qor, resources, and timing information needed to analyze the design.
report_area > logical_synthesis/reports/${file_name}_dcc_area.rpt
report_cell > logical_synthesis/reports/${file_name}_dcc_cells.rpt
report_power > logical_synthesis/reports/${file_name}_dcc_power.rpt
report_qor  > logical_synthesis/reports/${file_name}_dcc_qor.rpt
report_resources > logical_synthesis/reports/${file_name}_dcc_resources.rpt
report_timing -max_paths 10 > logical_synthesis/reports/${file_name}_dcc_timing.rpt


## Dump out the constraints in an SDC file
write_sdc  logical_synthesis/outputs/${file_name}.sdc


## Dump out the synthesized database and gate-level-netlist
write -f ddc -hierarchy -output logical_synthesis/outputs/${file_name}.ddc
write -hierarchy -format verilog -output logical_synthesis/outputs/${file_name}.v


exit

