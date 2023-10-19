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
import json
from datetime import datetime
import numpy as np

#The design class. this class holds all data for the current design that's being run. 
class Design:
    def __init__(self, design_name, run_count, input_delay, output_delay, set_clock_uncertainty):
        self.design_name = design_name
        self.run_count = run_count
        self.input_delay = input_delay
        self.output_delay = output_delay
        self.set_clock_uncertainty = set_clock_uncertainty

    def get_design_name(self):
        return self.design_name

    def get_run_count(self):
        return self.run_count

    def get_input_delay(self):
        return self.input_delay

    def get_output_delay(self):
        return self.output_delay

    def get_set_clock_uncertainty(self):
        return self.set_clock_uncertainty

    def set_design_name(self, design_name):
        self.design_name = design_name

    def set_run_count(self, run_count):
        self.run_count = run_count

    def set_input_delay(self, input_delay):
        self.input_delay = input_delay

    def set_output_delay(self, output_delay):
        self.output_delay = output_delay

    def set_set_clock_uncertainty(self, set_clock_uncertainty):
        self.set_clock_uncertainty = set_clock_uncertainty
    
    def get_instance(self):
        return self


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
work_dir = os.path.join(current_dir, "eda_pipeline_main","Synopsys_main", "Synopsys-eda-pipeline")
bulk_dir = os.path.join(work_dir, "bulk_configs")
script_dir = os.path.join(work_dir, "default_design/scripts")
default_dir = os.path.join(work_dir,"default_design/configs")
source_dir = os.path.join(work_dir, "source_files")
user_config_dir = os.path.join(current_dir,"Custom_Configs")

##############################################################
# Parse JSON Functions   
# ############################################################         
# These functions are used to parse the user-provided json file.
# JSON entries -> current_design Design class instance
# 
##############################################################
def pull_json(custom_user_config):
    user_config = os.path.join(user_config_dir,custom_user_config)
    with open(user_config) as json_file:
        data = json.load(json_file)
    return data

def parse_config_json(data):
## note: json contains floats or json contains integers that we turn into floats

    if "design_name" in data:
        design_name = list(data["design_name"])
    if "run_count" in data:
        run_count = data["run_count"]
    if "input_delay" in data:
        if "start" in data["input_delay"] and data["input_delay"]["start"]:
            in_delay = np.arange(data["input_delay"]["start"],data["input_delay"]["end"]+data["input_delay"]["step"],data["input_delay"]["step"]).tolist()
            #in_delay = list(range(data["input_delay"]["start"], data["input_delay"]["end"] + 1, data["input_delay"].get("step", 1)))
            #in_delay = np.linspace(data["input_delay"]["start"],data["input_delay"]["end"],data["input_delay"].get("step", 1))
        else:
            in_delay = list(data["input_delay"])
    if "output_delay" in data:
        if "start" in data["output_delay"] and data["output_delay"]["start"]:
            out_delay = np.arange(data["output_delay"]["start"],data["output_delay"]["end"]+data["output_delay"]["step"],data["output_delay"]["step"]).tolist()
            #out_delay = list(range(, data["output_delay"]["end"] + 1, data["output_delay"].get("step", 1)))
        else:
            out_delay = list(data["output_delay"])
    if "set_clock_uncertainty" in data:
        if "start" in data["set_clock_uncertainty"] and data["set_clock_uncertainty"]["start"]:
            set_clk_uncertainty = np.arange(data["set_clock_uncertainty"]["start"],data["set_clock_uncertainty"]["end"]+data["set_clock_uncertainty"]["step"],data["set_clock_uncertainty"]["step"]).tolist()
            #set_clk_uncertainty = list(range(data["set_clock_uncertainty"]["start"], data["set_clock_uncertainty"]["end"] + 1, data["set_clock_uncertainty"].get("step", 1)))
        else:
            set_clk_uncertainty = list(data["set_clock_uncertainty"])
    current_design = Design(design_name,run_count,in_delay,out_delay,set_clk_uncertainty)
    return current_design

##############################################################
# Create DEFAULT Configuration Files        
# ############################################################ 
# def create_configs_constraints_defaults():
# - If a design netlist hasn't been run before, it needs a "default" config & constraint
# 
##############################################################
def create_configs_constraints_defaults(design_name,dc_default_config,icc_default_config):
    with open(dc_default_config, "w") as f:
        f.write(f"set file_name {design_name}\n")
        f.write("set c_area_effort medium\n")
        f.write("set c_map_effort medium\n")
        f.write("set in_delay 0.1\n")
        f.write("set out_delay 0.1\n")
        f.write("set s_load 0.2\n")
        f.write("set s_clk_uncert 0.05\n")
    with open(icc_default_config, "w") as f:
        f.write(f"set file_name {design_name}\n")

##############################################################
# Create Synopsys Configuration Files       
# ############################################################
# def create_config_constraint_folder():
# - Creates time-stamped configuration folder
# def create_directory_tree()
# - Creates directory tree for Synopsys to populate
#
# The rest of the functions take parsed data and turn it into configs & constraints
# 
##############################################################
def create_config_constraint_folder(design_name):
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
    new_bulk = '{}_'.format(timestamp) + f"{design_name}"
    full_bulk_dir=os.path.join(bulk_dir,new_bulk)
    if not os.path.exists(full_bulk_dir):
        os.mkdir(full_bulk_dir)
    return full_bulk_dir

# Define a function to create the directory tree recursively
def create_directory_tree(directory_tree, parent_dir='.'):
    for name, children in directory_tree.items():
        dir_path = os.path.join(parent_dir, name)
        os.mkdir(dir_path)
        if children:
            create_directory_tree(children, dir_path)

def create_dc_configs(design_name,full_bulk_dir,current_design):
    area_effort = ["medium"]
    map_effort = ["medium"]
    input_delay = current_design.get_input_delay()
    output_delay = current_design.get_output_delay()
    set_load = ["0.2"]
    set_clock_uncertainty = current_design.get_set_clock_uncertainty()

    combinations = list(itertools.product(area_effort, map_effort,input_delay,output_delay,set_load,set_clock_uncertainty))

    for i, combo in enumerate(combinations):
        file_name = f"{full_bulk_dir}/dc_{design_name}_config_{i}.txt"
        with open(file_name, "w") as f:
            f.write(f"set file_name {design_name}\n")
            f.write(f"set c_area_effort {combo[0]}\n")
            f.write(f"set c_map_effort {combo[1]}\n")
            f.write(f"set in_delay {combo[2]}\n")
            f.write(f"set out_delay {combo[3]}\n")
            f.write(f"set s_load {combo[4]}\n")
            f.write(f"set s_clk_uncert {combo[5]}\n")

def create_icc_configs(design_name,full_bulk_dir,current_design):
    #area_effort = ["low", "medium","high"]
    #map_effort = ["medium", "high"]
    #input_delay = ["0.1","0.5","1.0","1.5","2.0"]
    #output_delay = ["0.1","0.5","1.0","1.5","2.0"]
    #set_load = ["0.2","0.3"]
    #set_clock_uncertainty = ["0.05","0.1"]

    combinations = list(itertools.product(design_name))

    for i, combo in enumerate(combinations):
        file_name = f"{full_bulk_dir}/icc_{design_name}_config_{i}.txt"
        with open(file_name, "w") as f:
            f.write(f"set file_name {combo[0]}\n")

##############################################################
# Run Synopsys Single Run       
# ############################################################
# def s_single_run_default_test():
# - Does a single run of the provided design name
# 
# More of a testing/debugging function for me :)
# 
##############################################################

def s_single_run_default_test(design_name,output_dir):
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

def s_bulk_run_test(design_name,new_bulk_dir,output_dir,run_count):
    for n in range(run_count):
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
        default_design_dir = os.path.join(default_dir,design_name)
        dc_default_design_config = os.path.join(default_dir,design_name,dc_default_config)
        icc_default_design_config = os.path.join(default_dir,design_name,icc_default_config)
        if not os.path.exists(default_design_dir):
            os.mkdir(default_design_dir)
            create_configs_constraints_defaults(design_name,dc_default_design_config,icc_default_design_config)

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
def read_file(design_name):
    with open(design_name, 'r') as f:
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

##############################################################
# Run the entire Synopsys pipeline using a user-created json  
# ############################################################
# def s_config_run():
# - Runs everything in the right order
# 
##############################################################
def s_config_run(output_dir,custom_user_json):
    data = pull_json(custom_user_json)
    #current_config_data = parse_config_json(data)
    current_project_data = parse_config_json(data)
    design_name_list = current_project_data.get_design_name()
    run_count = current_project_data.get_run_count()
    for name in design_name_list:
        full_bulk_dir = create_config_constraint_folder(name)
        #create_configs(full_bulk_dir,current_config_data)
        create_dc_configs(name,full_bulk_dir,current_project_data)
        s_bulk_run_test(name,full_bulk_dir,output_dir,run_count)




