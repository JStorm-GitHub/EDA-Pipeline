##############################################################
#           _                   _            _ _             #
#   ___  __| | __ _       _ __ (_)_ __   ___| (_)_ __   ___  #
#  / _ \/ _` |/ _` |_____| '_ \| | '_ \ / _ \ | | '_ \ / _ \ #
# |  __/ (_| | (_| |_____| |_) | | |_) |  __/ | | | | |  __/ #
#  \___|\__,_|\__,_|     | .__/|_| .__/ \___|_|_|_| |_|\___| #
#                        |_|     |_|                         #
##############################################################
### OpenROAD_main ###
    # John Storm #
    # ECE-34     #
    ##############



import os
import shutil
import subprocess
import itertools
import json
from datetime import datetime
import numpy as np
##############################################
# Set the correct path to openroad-flow-scripts/flow
##############################################
## path_to_flow = "/path/to/OpenROAD-flow-scripts/flow"
path_to_flow = "/home/js/A/OpenROAD-eda-pipeline/flow"


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

##############################################################
# Pathing Setup.
# ############################################################            
# These are the only "global" variables used in the pipeline
# 
##############################################################
current_dir = os.getcwd()
path_to_src = os.path.join(path_to_flow, "designs/src")
source_dir = os.path.join(current_dir,"eda_pipeline_main","source_files")
work_dir = os.path.join(current_dir, "eda_pipeline_main","OpenROAD_main", "OpenROAD-eda-pipeline")
bulk_dir = os.path.join(work_dir, "bulk_configs")
default_dir = os.path.join(work_dir,"default_design")
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
    ### Work in progress. No variables within the .mk file are editted so far
    core_utilization = ["60"]
    core_margin = ["5"]
    place_density_lb_addon = ["0.20"]
    custom_config_data = [core_utilization,core_margin,place_density_lb_addon]
    return custom_config_data
 
def parse_constraint_json(data):
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
# Prepare OpenROAD & Create DEFAULT Configuration Files        
# ############################################################
# def prepare_openroad():
# - OpenROAD requires the design.v (and any required modules i.e. dff.v) to be placed in 
#   a designs/src directory.
# 
# def create_configs_constraints_defaults():
# - If a design netlist hasn't been run before, it needs a "default" config & constraint
# 
##############################################################

def prepare_openroad(design_name):
    old_src_path = os.path.join(source_dir,f"{design_name}.v")
    dff_path = os.path.join(source_dir,"dff.v")
    new_src_path = os.path.join(path_to_src,design_name)
    if not os.path.exists(new_src_path):
        try:
            os.mkdir(new_src_path)
            print(f"Created {new_src_path}")
        except OSError as e:
            print(f"Failed to create directory: {e}.\n Check that you've set OpenROAD_eda_pipeline.py's path_to_flow variable to the correct path")
    shutil.copy(old_src_path,new_src_path)
    shutil.copy(dff_path,new_src_path)

def create_configs_constraints_defaults(design_name,default_config,default_constraint):
    # Create default config .mk
    #default_config = f"{default_dir}/{design_name}/{design_name}_default_config.mk"
    with open(default_config, "w") as f:
        f.write("export PLATFORM = sky130hd\n")
        f.write(f"export DESIGN_NAME = {design_name}\n")
        f.write(f"export DESIGN_NICKNAME = {design_name}\n")
        f.write("export VERILOG_FILES = $(sort $(wildcard ./designs/src/$(DESIGN_NICKNAME)/*.v))\n")
        f.write("mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))\n")
        f.write("mkfile_dir := $(dir $(mkfile_path))\n")
        f.write("export SDC_FILE      = $(mkfile_dir)/*.sdc\n")
        f.write("export CORE_UTILIZATION = 60\n")
        f.write("export CORE_MARGIN = 5\n")
        f.write("export PLACE_DENSITY_LB_ADDON = 0.20\n")
    # Create default constraint .sdc
    #default_constraint = f"{default_dir}/{design_name}/{design_name}_default_sdc.sdc"
    with open(default_constraint, "w") as f:
        f.write(f"current_design {design_name}\n")
        f.write("\n")
        f.write("set clk_name clk\n")
        f.write("set clk_port_name clk\n")
        f.write("set clk_period 1.0\n")
        f.write("set clk_io_pct 0.2\n")
        f.write("\n")
        f.write("set clk_port [get_ports $clk_port_name]\n")
        f.write("\n")
        f.write("create_clock -name $clk_name -period $clk_period $clk_port\n")
        f.write("\n")
        f.write("set non_clock_inputs [lsearch -inline -all -not -exact [all_inputs] $clk_port]\n")
        f.write("\n")
        f.write("set_input_delay  [expr $clk_period * $clk_io_pct] -clock $clk_name $non_clock_inputs\n")
        f.write("set_output_delay [expr $clk_period * $clk_io_pct] -clock $clk_name [all_outputs]\n")

##############################################################
# Create OpenROAD Configuration Files       
# ############################################################
# def create_config_constraint_folder():
# - Creates time-stamped configuration folder
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


def create_configs(design_name,full_bulk_dir,custom_config_data):
    core_utilization = custom_config_data[0]
    core_margin = custom_config_data[1]
    place_density_lb_addon = custom_config_data[2]

    combinations = list(itertools.product(core_utilization,core_margin,place_density_lb_addon))

    for i, combo in enumerate(combinations):
        file_name = f"{full_bulk_dir}/{design_name}_config_{i}.mk"
        with open(file_name, "w") as f:
            f.write("export PLATFORM = sky130hd\n")
            f.write(f"export DESIGN_NAME = {design_name}\n")
            f.write(f"export DESIGN_NICKNAME = {design_name}\n")
            f.write("export VERILOG_FILES = $(sort $(wildcard ./designs/src/$(DESIGN_NICKNAME)/*.v))\n")
            f.write("mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))\n")
            f.write("mkfile_dir := $(dir $(mkfile_path))\n")
            f.write("export SDC_FILE      = $(mkfile_dir)/*.sdc\n")
            f.write(f"export CORE_UTILIZATION = {combo[0]}\n")
            f.write(f"export CORE_MARGIN = {combo[1]}\n")
            f.write(f"export PLACE_DENSITY_LB_ADDON = {combo[2]}\n")


def create_constraints(design_name,full_bulk_dir,current_design):
    #design_name = current_design.get_design_name()
    clk_period = ["1.0"]
    clk_io_pct = ["0.2"]
    in_delay = current_design.get_input_delay()
    out_delay = current_design.get_output_delay()
    set_clk_uncertainty = current_design.get_set_clock_uncertainty()
    # in_delay=["0.1","0.5","1.0","1.5","2.0"]
    # out_delay=["0.1","0.5","1.0","1.5","2.0"]
    # set_clk_uncertainty=["0.05","0.1"]

    combinations = list(itertools.product(clk_period,clk_io_pct,in_delay,out_delay,set_clk_uncertainty))

    for i, combo in enumerate(combinations):
        file_name = f"{full_bulk_dir}/{design_name}_sdc_{i}.sdc"
        with open(file_name, "w") as f:
            f.write(f"current_design {design_name}\n")
            f.write("\n")
            f.write("set clk_name clk\n")
            f.write("set clk_port_name clk\n")
            f.write(f"set clk_period {combo[0]}\n")
            f.write(f"set clk_io_pct {combo[1]}\n")
            f.write("\n")
            f.write("set clk_port [get_ports $clk_port_name]\n")
            f.write("\n")
            f.write("create_clock -name $clk_name -period $clk_period $clk_port\n")
            f.write("\n")
            f.write("set non_clock_inputs [lsearch -inline -all -not -exact [all_inputs] $clk_port]\n")
            f.write("\n")
            f.write("set_input_delay  [expr $clk_period * $clk_io_pct] -clock $clk_name $non_clock_inputs\n")
            f.write("set_output_delay [expr $clk_period * $clk_io_pct] -clock $clk_name [all_outputs]\n")
            f.write("\n")
            f.write(f"set_input_delay -clock [get_clocks clk] -add_delay {combo[2]} [all_inputs]\n")
            f.write(f"set_output_delay -clock [get_clocks clk] -add_delay {combo[3]} [all_outputs]\n")
            f.write("\n")
            f.write(f"set_clock_uncertainty {combo[4]} [all_clocks]\n")

##############################################################
# Run OpenROAD Single Run       
# ############################################################
# def o_single_run_default_test():
# - Does a single run of the provided design name
# 
# More of a testing/debugging function for me.
# 
##############################################################

def o_single_run_default_test(design_name,output_dir):
    # Create design folder in OpenROAD-flow-scripts/flow/designs/src for design
    prepare_openroad(design_name)

    design_variant = f"{design_name}_default"    #the name of the compilation run
    variant_dir = f"openroad_{design_variant}"    #the directory containing this run

    default_config = f"{design_name}_default_config.mk"

    default_constraint= f"{design_name}_default_sdc.sdc"
    work_home = os.path.join(output_dir, variant_dir)

    default_design_config = os.path.join(default_dir,design_name,default_config)
    default_design_constraint = os.path.join(default_dir,design_name,default_constraint)

    if not os.path.exists(f"{work_home}"):
        os.mkdir(f"{work_home}")
    else:
        print("Design has already been run")
        return None


    #copy over defaults
    shutil.copy(default_design_config,work_home)
    design_config = os.path.join(work_home,default_config)
    shutil.copy(default_design_constraint,work_home)

    run_design(design_config,work_home,design_variant)

##############################################################
# Run OpenROAD Bulk Run       
# ############################################################
# def o_bulk_run_test():
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

def o_bulk_run_test(design_name,new_bulk_dir,output_dir,run_count):

    for n in range(run_count):
        # Set the name of the directory & design
        design_variant = f"{design_name}_{n}"    #the name of the compilation run
        variant_dir = f"openroad_{design_variant}"    #the directory containing this run

        #configs
        variant_config = f"{design_name}_config_{n}.mk"     #define what the config name should be
        default_config = f"{design_name}_default_config.mk"

        #sdc constraints
        variant_constraint= f"{design_name}_sdc_{n}.sdc"
        default_constraint = f"{design_name}_default_sdc.sdc"


        work_home = os.path.join(output_dir, variant_dir)    #full path for outputted variant directory

        bulk_design_config = os.path.join(new_bulk_dir, variant_config) #full path for bulk-created variant config
        bulk_design_constraint = os.path.join(new_bulk_dir, variant_constraint) #full path for bulk-created variant sdc

        #defaults
        default_design_dir = os.path.join(default_dir,design_name)
        default_design_config = os.path.join(default_design_dir,default_config)
        default_design_constraint = os.path.join(default_design_dir,default_constraint)
        ### checks if defaults exist
        if not os.path.exists(default_design_dir):
            os.mkdir(default_design_dir)
            create_configs_constraints_defaults(design_name,default_design_config,default_design_constraint)
        


        if not os.path.exists(f"{work_home}"):
            os.mkdir(f"{work_home}")

        #copy over mk file for this variant

        #uses bulk-created config if available
        if os.path.exists(bulk_design_config):
            shutil.copy(bulk_design_config, work_home)
            design_config = os.path.join(work_home,variant_config)
        else:
            shutil.copy(default_design_config,work_home)
            design_config = os.path.join(work_home,default_config)

        #uses bulk-created constraint if available
        if os.path.exists(bulk_design_constraint):
            shutil.copy(bulk_design_constraint, work_home)
        else:
            shutil.copy(default_design_constraint,work_home)

        run_design(design_config,work_home,design_variant)

##############################################################
# Run Design  
# ############################################################
# def run_design():
# - Points OpenROAD's makefile towards the directories generated so far. 
#   Important to 
# 
# - Arguments:
#   - design_config: The design configuration file for current design
#   - work_home: The directory we created & copied config files in the previous functions
#   - design_variant: Correctly names the files OpenROAD outputs
# 
##############################################################

def run_design(design_config,work_home,design_variant):
    print("Compiled " + design_config+" in " +work_home + " for "+design_variant)
    #os.chdir(path_to_flow)
    #process = subprocess.Popen(["make", f"DESIGN_CONFIG={design_config}", f"WORK_HOME={work_home}", f"FLOW_VARIANT={design_variant}"])
    #exit_code = process.wait()
    #os.chdir(current_dir)

##############################################################
# Run the entire OpenROAD pipeline using a user-created json  
# ############################################################
# def o_config_run():
# - Runs everything in the right order
# 
##############################################################


def o_config_run(output_dir,custom_user_json):
    data = pull_json(custom_user_json)
    current_config_data = parse_config_json(data)
    current_constraint_data = parse_constraint_json(data)
    design_name_list = current_constraint_data.get_design_name()
    run_count = current_constraint_data.get_run_count()
    for name in design_name_list:
        prepare_openroad(name)
        full_bulk_dir = create_config_constraint_folder(name)
        #create_configs(full_bulk_dir,current_config_data)
        create_constraints(name,full_bulk_dir,current_constraint_data)
        o_bulk_run_test(name,full_bulk_dir,output_dir,run_count)

