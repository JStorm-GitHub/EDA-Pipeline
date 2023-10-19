##############################################################
#           _                   _            _ _             #
#   ___  __| | __ _       _ __ (_)_ __   ___| (_)_ __   ___  #
#  / _ \/ _` |/ _` |_____| '_ \| | '_ \ / _ \ | | '_ \ / _ \ #
# |  __/ (_| | (_| |_____| |_) | | |_) |  __/ | | | | |  __/ #
#  \___|\__,_|\__,_|     | .__/|_| .__/ \___|_|_|_| |_|\___| #
#                        |_|     |_|                         #
##############################################################
### Synopsys_main ###
    # John Storm #
    # ECE-34     #
    ##############
### offline-debug (for when you can't access the tools)
DEBUG = True
###




import os
import shutil
import subprocess
import itertools
from datetime import datetime

# Define the directory tree structure used by create_directory_tree()
directory_tree = {
    'cts': {
        'reports': {},
        'outputs': {},
    },
    'extracted': {
        'reports': {},
        'outputs': {},
    },
    'final': {
        'reports': {},
        'outputs': {},
    },
    'floorplan': {
        'reports': {},
        'outputs': {},
    },
    'logical_synthesis': {
        'reports': {},
        'outputs': {},
    },
    'placed': {
        'reports': {},
        'outputs': {},
    },
    'routed': {
        'reports': {},
        'outputs': {},
    },
}

##############################################################
# Pathing Setup.
# ############################################################
# These are the only "global" variables used in the pipeline
#
##############################################################
current_dir = os.getcwd()
output_dir = os.path.join(current_dir,"Outputs")
work_dir = os.path.join(current_dir, "eda_pipeline_main","Synopsys_main", "Synopsys-eda-pipeline")
bulk_dir = os.path.join(work_dir, "bulk_configs")
script_dir = os.path.join(work_dir, "default_design/scripts")
default_dir = os.path.join(work_dir,"default_design/configs")
source_dir = os.path.join(work_dir, "source_files")


##############################################################
# Create Synopsys Configuration Files
# ############################################################
# def create_directory_tree()
# - Creates directory tree for Synopsys to populate
#
# The rest of the functions take parsed data and turn it into configs & constraints
#
##############################################################
def create_bulk_configs(filename):

    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
    new_bulk = f"{filename}"+'_{}'.format(timestamp)
    full_bulk_dir=os.path.join(bulk_dir,new_bulk)
    if not os.path.exists(full_bulk_dir):
        os.mkdir(full_bulk_dir)

    area_effort = ["low", "medium","high"]
    map_effort = ["medium", "high"]
    input_delay = ["0.1","0.5","1.0","1.5","2.0"]
    output_delay = ["0.1","0.5","1.0","1.5","2.0"]
    set_load = ["0.2","0.3"]
    set_clock_uncertainty = ["0.05","0.1"]

    combinations = list(itertools.product(area_effort, map_effort,input_delay,output_delay,set_load,set_clock_uncertainty))

    for i, combo in enumerate(combinations):
        file_name = f"{full_bulk_dir}/dc_{filename}_config_{i}.txt"
        with open(file_name, "w") as f:
            f.write(f"set file_name {filename}\n")
            f.write(f"set c_area_effort {combo[0]}\n")
            f.write(f"set c_map_effort {combo[1]}\n")
            f.write(f"set in_delay {combo[2]}\n")
            f.write(f"set out_delay {combo[3]}\n")
            f.write(f"set s_load {combo[4]}\n")
            f.write(f"set s_clk_uncert {combo[5]}\n")
    
    ### SPACE EMPTY FOR ICC_CONFIG GENERATION
    
    return full_bulk_dir

# Define a function to create the directory tree recursively
def create_directory_tree(directory_tree, parent_dir='.'):
    for name, children in directory_tree.items():
        dir_path = os.path.join(parent_dir, name)
        os.mkdir(dir_path)
        if children:
            create_directory_tree(children, dir_path)

##############################################################
# Run Synopsys Single Run
# ############################################################
# def s_single_run_default_test():
# - Does a single run of the provided design name
#
# More of a testing/debugging function for me :)
#
##############################################################
def s_single_run_default(design_name):
    design_variant = f"{design_name}_default"    #the name of the compilation run
    variant_dir = f"synopsys_{design_variant}"    #the directory containing this run
    source_file = os.path.join(source_dir, design_name + '.v')
    source_dff = os.path.join(source_dir,"dff.v")


    dc_default_config = f"dc_{design_name}_default_config.txt"
    icc_default_config = f"icc_{design_name}_default_config.txt"

    work_home = os.path.join(output_dir, variant_dir)    #full path for outputted variant directory
    dc_default_design_config = os.path.join(default_dir,design_name,dc_default_config)
    icc_default_design_config = os.path.join(default_dir,design_name,icc_default_config)

    if not os.path.exists(f"{work_home}"):
        os.mkdir(f"{work_home}")
    else:
        print("Design has already been run")
        return None

    #default dc_config copy
    shutil.copy(dc_default_design_config,work_home)
    dc_design_config = dc_default_config

    #default icc_config copy
    shutil.copy(icc_default_design_config,work_home)
    icc_design_config = icc_default_config

    #tcl script copy
    script_dest = os.path.join(work_home,"scripts")
    shutil.copytree(script_dir, script_dest)

    #source copy
    src_dest = os.path.join(work_home,"src")
    os.mkdir(src_dest)
    shutil.copy(source_file,src_dest)
    shutil.copy(source_dff,src_dest)

    os.chdir(work_home)
    create_directory_tree(directory_tree)
    run_design(dc_design_config,icc_design_config)
    os.chdir(current_dir)

##############################################################
# Run Synopsys Bulk Run
# ############################################################
# def s_bulk_run_test():
# - Does a bulk run of the provided design name
#
# The work-horse of the eda-pipeline.
#
# - Arguments:
#   - design_name: The name of the netlist used in the run
#       - ex: s386
#   - new_bulk_dir: The time-stamped bulk-configuration file made by
#       create_config_constraint_folder()
#       - ex: 2023-05-22_17-04-33_s838
#   - output_dir: The time-stamped output directory created by eda-pipeline.py (main)
#   - run_count: The run_count from the json.
#
##############################################################
def s_bulk_run(design_name):

    new_bulk_dir=create_bulk_configs(design_name)

    i = 3

    for n in range(i):

        # Set the name of the directory & design
        design_variant = f"{design_name}_{n}"    #the name of the compilation run
        variant_dir = f"synopsys_{design_variant}"    #the directory containing this run
        source_file = os.path.join(source_dir, design_name + '.v')
        source_dff = os.path.join(source_dir, "dff.v")



    #configs
        #dc
        dc_variant_config = f"dc_{design_name}_config_{n}.txt"     #define what the config name should be
        dc_default_config = f"dc_{design_name}_default_config.txt"
        #icc
        icc_variant_config = f"icc_{design_name}_config_{n}.txt"     #define what the config name should be
        icc_default_config = f"icc_{design_name}_default_config.txt"

        work_home = os.path.join(output_dir, variant_dir)    #full path for outputted variant directory
        dc_bulk_design_config = os.path.join(new_bulk_dir, dc_variant_config) #full path for bulk-created dc config
        icc_bulk_design_config = os.path.join(new_bulk_dir, icc_variant_config) #full path for bulk-created icc config

    #defaults
        dc_default_design_config = os.path.join(default_dir,design_name,dc_default_config)
        icc_default_design_config = os.path.join(default_dir,design_name,icc_default_config)


        if not os.path.exists(f"{work_home}"):
            os.mkdir(f"{work_home}")
        else:
            continue

        if os.path.exists(dc_bulk_design_config):
            shutil.copy(dc_bulk_design_config, work_home)
            dc_design_config = dc_variant_config
        else:
            shutil.copy(dc_default_design_config,work_home)
            dc_design_config = dc_default_config

        if os.path.exists(icc_bulk_design_config):
            shutil.copy(icc_bulk_design_config, work_home)
            icc_design_config = icc_variant_config
        else:
            shutil.copy(icc_default_design_config,work_home)
            icc_design_config = icc_default_config

        #tcl script copy
        script_dest = os.path.join(work_home,"scripts")
        shutil.copytree(script_dir, script_dest)

        #source copy
        src_dest = os.path.join(work_home,"src")
        os.mkdir(src_dest)
        shutil.copy(source_file,src_dest)
        shutil.copy(source_dff,src_dest)

        os.chdir(work_home)
        create_directory_tree(directory_tree)

        run_design(dc_design_config,icc_design_config)

        os.chdir(current_dir)


##############################################################
# Run Design
# ############################################################
# def run_design():
# - Points OpenROAD's makefile towards the directories generated so far.
#   Important to
#
# - Arguments:
#   - dc_design_config: The dc design configuration file for current design
#   - icc_design_config: The ic design configuration file for current design
#
# Rest of the functions are for clean code
#
##############################################################
def read_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def join_list_with_delimiter(input_list):
    return "; ".join(input_list)

def run_design(dc_design_config,icc_design_config):
    gui_enable = ["-gui"]

    #declares dc_synth tcl file
    d_synth_tcl = "scripts/d_synth.tcl"
    dc_tcl_command = ["-f", d_synth_tcl]

    #declares dc_shell
    dc_shell = "dc_shell"
    dc_shell_command = [dc_shell]

    #declares additional dc commands
    dc_additional_commands = join_list_with_delimiter(read_file(dc_design_config))
    dc_command_list = ["-x",dc_additional_commands]

    dc_full_command_list = (dc_shell_command+dc_command_list)+dc_tcl_command

    #add gui_enable
    #dc_full_command_list = dc_full_command_list+gui_enable

    print(dc_full_command_list)

    if not DEBUG:
        subprocess.call(dc_full_command_list)

    print("Logical Synthesis complete.")

    #declares icc_synth tcl file
    icc_synth_tcl = "scripts/run.tcl"
    icc_tcl_command = ["-f", icc_synth_tcl]

    #declares icc_shell
    icc_shell = "icc_shell"
    icc_shell_command = [icc_shell, "-shared_license"]

    #declares additional icc commands
    icc_additional_commands = join_list_with_delimiter(read_file(icc_design_config))
    icc_command_list = ["-x",icc_additional_commands]

    icc_full_command_list = (icc_shell_command+icc_command_list)+icc_tcl_command
    #icc_full_command_list = icc_full_command_list + gui_enable

    print(icc_full_command_list)

    if not DEBUG:
        subprocess.call(icc_full_command_list)

    print("ICC compilation complete.")


