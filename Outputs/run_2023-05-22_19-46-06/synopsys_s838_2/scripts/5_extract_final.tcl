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
