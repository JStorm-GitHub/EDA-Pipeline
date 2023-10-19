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
