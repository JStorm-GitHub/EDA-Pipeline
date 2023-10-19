##############################################################
#           _                   _            _ _             #
#   ___  __| | __ _       _ __ (_)_ __   ___| (_)_ __   ___  #
#  / _ \/ _` |/ _` |_____| '_ \| | '_ \ / _ \ | | '_ \ / _ \ #
# |  __/ (_| | (_| |_____| |_) | | |_) |  __/ | | | | |  __/ #
#  \___|\__,_|\__,_|     | .__/|_| .__/ \___|_|_|_| |_|\___| #
#                        |_|     |_|                         #
##############################################################
     ### MAIN ###
    # John Storm #
    # ECE-34     #
    ##############

import os
import threading
from datetime import datetime

from eda_pipeline_main.Synopsys_main.Synopsys_eda_pipeline import s_single_run_default, s_bulk_run
from eda_pipeline_main.OpenROAD_main.OpenROAD_eda_pipeline import o_single_run_default, o_bulk_run

from eda_pipeline_main.OpenROAD_main.OpenROAD_eda_pipeline_test import o_config_run
from eda_pipeline_main.Synopsys_main.Synopsys_eda_pipeline_test import s_config_run




current_dir = os.getcwd()
path_to_source = os.path.join(current_dir,"eda_pipeline_main","source_files")
output_dir = os.path.join(current_dir,"Outputs")

user_json = 'test_run.json'

##############################################################
# Creates a time-stamped directory for the current run   
# ############################################################
# def make_time_stamped_output():
# - Returns the name of the time-stamped directory so it can be output 
#   downstream in the pipeline.
# 
##############################################################
def make_time_stamped_output():
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
    new_output = "run_{}".format(timestamp)
    full_output_dir=os.path.join(current_dir,output_dir,new_output)
    if not os.path.exists(full_output_dir):
        os.mkdir(full_output_dir)
    return full_output_dir

##############################################################
# Run the entire pipeline using CLI prompts or user-created json  
# ############################################################
# Single, bulk, and parallelized
# 
##############################################################
while True:
    current_dir = os.getcwd()
    path_to_source = os.path.join(current_dir,"eda_pipeline_main","source_files")
    output_dir = os.path.join(current_dir,"Outputs")
    # Ask the user for the design name
    design_name = input("Enter the name of a design or type 'custom' and use  (or type 'exit' to quit): ")
    if design_name == 'exit':
        break
    if design_name == 'custom':
        output_dir = make_time_stamped_output()
        t1 = threading.Thread(target= o_config_run, args=(output_dir,user_json))
        t2 = threading.Thread(target= s_config_run, args=(output_dir,user_json))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        continue
    # Check if the design file exists
    design_file = os.path.join(path_to_source, design_name + '.v')
    if not os.path.exists(design_file):
        print("That design file isn't in the pipeline. Please add it to the " + path_to_source + " directory")
    else:
        # Ask the user for the process type
        process_type = input("Enter 'single' for a single process or 'bulk' for a bulk process: ")

        # Perform the process
        if process_type == 'single':
            tool = input("Enter 's' for Synopsys, 'o' for OpenROAD, or 'os'/'so' for both: ")
            if tool not in ['s', 'o', 'os', 'so']:
                print("Invalid tool. Please enter 's', 'o', 'os', or 'so'.")
                continue
            if tool == 's':
                s_single_run_default(design_name)
                continue
            elif tool == 'o':
                o_single_run_default(design_name)
                continue
            else:
                t1 = threading.Thread(target= s_single_run_default, args=(design_name,))
                t2 = threading.Thread(target= o_single_run_default, args=(design_name,))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
                continue
        elif process_type == 'bulk':
            tool = input("Enter 's' for Synopsys, 'o' for OpenROAD, or 'os'/'so' for both: ")
            if tool not in ['s', 'o', 'os', 'so']:
                print("Invalid tool. Please enter 's', 'o', 'os', or 'so'.")
                continue
            if tool == 's':
                #output_dir = make_time_stamped_output()
                s_bulk_run(design_name)
                continue
            elif tool == 'o':
                #output_dir = make_time_stamped_output()
                o_bulk_run(design_name)
                continue
            else:
                #output_dir = make_time_stamped_output()
                t1 = threading.Thread(target= s_bulk_run, args=(design_name,))
                t2 = threading.Thread(target= o_bulk_run, args=(design_name,))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
                continue
        else:
            print("Invalid process type. Please enter 'single' or 'bulk'.")
