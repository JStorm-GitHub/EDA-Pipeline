import os
import subprocess
dc_command_file = "dc_command_list.txt"
icc_command_file = "icc_command_list.txt"

def read_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def join_list_with_delimiter(input_list):
    return "; ".join(input_list)

gui_enable = ["-gui"]

#declares dc_synth tcl file
d_synth_tcl = "d_synth.tcl"
dc_tcl_command = ["-f", d_synth_tcl]

#declares dc_shell
dc_shell = "dc_shell"
dc_shell_command = [dc_shell]

#declares additional dc commands
dc_additional_commands = join_list_with_delimiter(read_file(dc_command_file))
dc_command_list = ["-x",dc_additional_commands]

dc_full_command_list = (dc_shell_command+dc_command_list)+dc_tcl_command

#add gui_enable
dc_full_command_list = dc_full_command_list+gui_enable

print(dc_full_command_list)

subprocess.call(dc_full_command_list)

print("Logical Synthesis complete.")

#declares icc_synth tcl file
icc_synth_tcl = "icc_synth.tcl"
icc_tcl_command = ["-f", icc_synth_tcl]

#declares icc_shell
icc_shell = "icc_shell"
icc_shell_command = [icc_shell, "-shared_license"]

#declares additional icc commands
icc_additional_commands = join_list_with_delimiter(read_file(icc_command_file))
icc_command_list = ["-x",icc_additional_commands]

icc_full_command_list = (icc_shell_command+icc_command_list)+icc_tcl_command
icc_full_command_list = icc_full_command_list + gui_enable

print(icc_full_command_list)

subprocess.call(icc_full_command_list)

print("ICC compilation complete.")

