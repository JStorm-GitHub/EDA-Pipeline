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
### offline-debug (for when you can't access the tools)
DEBUG = True
###





import os
import shutil
import subprocess
import itertools
from datetime import datetime
import numpy as np



##############################################################
# Pathing Setup.
# ############################################################
# These are the only "global" variables used in the pipeline
#
##############################################################

##############################################
# Set the correct path to openroad-flow-scripts/flow
##############################################
## path_to_flow = "/path/to/OpenROAD-flow-scripts/flow"
path_to_flow = "/home/js4684@drexel.edu/OpenROAD-flow-scripts/flow"

current_dir = os.getcwd()
output_dir = os.path.join(current_dir,"Outputs")
work_dir = os.path.join(current_dir, "eda_pipeline_main","OpenROAD_main", "OpenROAD-eda-pipeline")
bulk_dir = os.path.join(work_dir, "bulk_configs")
default_dir = os.path.join(work_dir,"default_design")

##############################################################
# Create OpenROAD Configuration Files
# ############################################################
# def create_bulk_configs():
# - Creates time-stamped configuration folder
#
# The rest of the functions take parsed data and turn it into configs & constraints
#
##############################################################
def create_bulk_configs(filename):

    # if not os.path.exists("bulk_configs"):
    #     os.mkdir("bulk_configs")
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
    new_bulk = f"{filename}"+'_{}'.format(timestamp)
    full_bulk_dir=os.path.join(bulk_dir,new_bulk)
    if not os.path.exists(full_bulk_dir):
        os.mkdir(full_bulk_dir)

    #filename = "s386"
    core_utilization = ["60"]
    core_margin = ["5"]
    place_density_lb_addon = ["0.20"]

    combinations = list(itertools.product(core_utilization,core_margin,place_density_lb_addon))

    for i, combo in enumerate(combinations):
        file_name = f"{full_bulk_dir}/{filename}_config_{i}.mk"
        with open(file_name, "w") as f:
            f.write("export PLATFORM = sky130hd\n")
            f.write(f"export DESIGN_NAME = {filename}\n")
            f.write(f"export DESIGN_NICKNAME = {filename}\n")
            f.write("export VERILOG_FILES = $(sort $(wildcard ./designs/src/$(DESIGN_NICKNAME)/*.v))\n")
            #f.write(f"export SDC_FILE      = ./eda-pipeline/bulk_configs/{filename}_sdc_{i}.sdc\n")
            f.write("mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))\n")
            f.write("mkfile_dir := $(dir $(mkfile_path))\n")
            f.write("export SDC_FILE      = $(mkfile_dir)/*.sdc\n")
            f.write(f"export CORE_UTILIZATION = {combo[0]}\n")
            f.write(f"export CORE_MARGIN = {combo[1]}\n")
            f.write(f"export PLACE_DENSITY_LB_ADDON = {combo[2]}\n")


    clk_period = "1.0"
    clk_io_pct = "0.2"
    in_delay=["0.1","0.5","1.0","1.5","2.0"]
    out_delay=["0.1","0.5","1.0","1.5","2.0"]
    set_clk_uncertainty=["0.05","0.1"]

    combinations = list(itertools.product(in_delay,out_delay,set_clk_uncertainty))

    for i, combo in enumerate(combinations):
        file_name = f"{full_bulk_dir}/{filename}_sdc_{i}.sdc"
        with open(file_name, "w") as f:
            f.write(f"current_design {filename}\n")
            f.write("\n")
            f.write("set clk_name clk\n")
            f.write("set clk_port_name clk\n")
            f.write(f"set clk_period {clk_period}\n")
            f.write(f"set clk_io_pct {clk_io_pct}\n")
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
            f.write(f"set_input_delay -clock [get_clocks clk] -add_delay {combo[0]} [all_inputs]\n")
            f.write(f"set_output_delay -clock [get_clocks clk] -add_delay {combo[1]} [all_outputs]\n")
            f.write("\n")
            f.write(f"set_clock_uncertainty {combo[2]} [all_clocks]\n")

    return full_bulk_dir




##############################################################
# Run OpenROAD Single Run
# ############################################################
# def o_single_run_default_test():
# - Does a single run of the provided design name
#
# More of a testing/debugging function for me :)
#
##############################################################
def o_single_run_default(design_name):
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
def o_bulk_run(design_name):
    # Set the number of directories to create
    i = 3
    # Set the base directory for the OpenROAD designs

    #design_name = "s386"
    #generate bulk_configs w/ create_bulk_configs.py
    new_bulk_dir=create_bulk_configs(design_name)
    for n in range(i):
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
        default_design_config = os.path.join(default_dir,design_name,default_config)
        default_design_constraint = os.path.join(default_dir,design_name,default_constraint)

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



def run_design(design_config,work_home,design_variant):
    print("Compiled " + design_config+" in " +work_home + " for "+design_variant)
    if not DEBUG:
        os.chdir(path_to_flow)
        process = subprocess.Popen(["make", f"DESIGN_CONFIG={design_config}", f"WORK_HOME={work_home}", f"FLOW_VARIANT={design_variant}"])
        exit_code = process.wait()
        os.chdir(current_dir)

