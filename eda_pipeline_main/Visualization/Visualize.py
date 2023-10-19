import sys
import csv
import os


# Define the table data as a list of lists
table_data = [
    ["Parameters", "Values", "# of Samples"],
    ["Compile Area Effort", "{low, medium, high}", "N/A"],
    ["Compile Map Effort", "{low, medium, high}", "N/A"],
    ["Input Delay", "{0.1, 0.5, 1}", "N/A"],
    ["Output Delay", "{0.1, 0.5, 1}", "N/A"],
    ["Set Load", "{0.2, 0.3}", "N/A"],
    ["Clock Uncertainity", "{0.05, 0.1}", "N/A"]
]

# Determine the maximum width of each column
col_widths = [max(len(str(item)) for item in col) for col in zip(*table_data)]

# Print the table header
print("-" * sum(col_widths))
print(" | ".join(str(item).ljust(width) for item, width in zip(table_data[0], col_widths)))
print("-" * sum(col_widths))

# Print the table rows
for row in table_data[1:]:
    print(" | ".join(str(item).ljust(width) for item, width in zip(row, col_widths)))

# Print the table footer
print("-" * sum(col_widths))
print("")

# Select if you want specific parameter values or just default values
Parameters = ["Compile Area Effort", "Compile Map Effort", "Input Delay", "Output Delay", "Set Load", "Clock Uncertainity", "Default"]
selected_parameters = input("Select the parameter you want to specify, or just hit enter to evaluate all: ")

if selected_parameters == "Compile Area Effort":
    selected_parameters = "c_area_effort"
    selected_parameters_value = input("Select the value for the parameter that you want to evaluate: ")
elif selected_parameters == "Compile Map Effort":
    selected_parameters = "c_map_effort"
    selected_parameters_value = input("Select the value for the parameter that you want to evaluate: ") 
elif selected_parameters == "Input Delay":
    selected_parameters = "in_delay"
    selected_parameters_value = input("Select the value for the parameter that you want to evaluate: ")
    selected_parameters_value = float(selected_parameters_value)
elif selected_parameters == "Output Delay":
    selected_parameters = "out_delay"
    selected_parameters_value = input("Select the value for the parameter that you want to evaluate: ")
    selected_parameters_value = float(selected_parameters_value) 
elif selected_parameters == "Set Load":
    selected_parameters = "s_load"
    selected_parameters_value = input("Select the value for the parameter that you want to evaluate: ")
    selected_parameters_value = float(selected_parameters_value)   
elif selected_parameters == "Clock Uncertainity":
    selected_parameters = "s_clk_uncert"
    selected_parameters_value = input("Select the value for the parameter that you want to evaluate: ")
    selected_parameters_value = float(selected_parameters_value)

# Select the circuit that you want to be evaluated:
all_circuits = ["s386", "s838"]
print("The following are the circuits that you can choose from: ", all_circuits, "\n")
circuit_str = input("Select the circuit(s) that you want to be evaluated, seperate by a comma if more than 1 (example: s386, s838): ")

# Split the input into a list of circuit names
circuit_list = circuit_str.split(",")
# Validate each input phase against the list of circuits
selected_circuits = []
for circuit in circuit_list:
    circuit = circuit.strip()
    if circuit in all_circuits and circuit not in selected_circuits:
        selected_circuits.append(circuit)
    else:
        print("Invalid circuit: \n", circuit)
        

# How to select the phase for the circuit to be evaluated
all_phases = ["placement", "logical_synthesis", "routed", "cts", "final"]
print("The following are the phases of circuit(s) that you can choose from: ", all_phases, "\n")
selected_phases = input("Select the phase(s) that you want to be evaluated: ") #, seperate by a comma if more than 1 (example: placement, final)
#phases_str = input("Select the phase(s) that you want to be evaluated, seperate by a comma if more than 1 (example: placement, final): ")
#phases_list = phases_str.split(",")
#selected_phases = []
#for phase in phases_list:
#    phase = phase.strip()
 #   if phase in all_phases and phase not in selected_phases:
#        selected_phases.append(phase)
 #   else:
 #       print("Invalid phase: \n", phase)

while selected_phases not in all_phases:
    print ("Invalid phase.\n")
    selected_phases = input("Select the phase(s) that you want to be evaluated: ") #, seperate by a comma if more than 1 (example: placement, final)


# How to select the metric to generate plot for
all_metrics = ["cell_area", "design_area", "levels_of_logic", "logic_optimization", "mapping_optimization", "net_area", "net_length_", "net_xlength_", 
               "net_ylength_", "overall_compile_time", "overall_clock_compile_wall_clock_time", "total_buffer_area", "total_inverter_area", "leakage_combinational",
               "leakage_register", "switching_combinational", "switching_register", "total_power"]
print("The following are the metrics of circuit(s) that you can choose from: ", all_metrics, "\n")
metric_str = input("Select the metric(s) that you want to be evaluated, seperate by a comma if more than 1 (example: design_area, other_metric): ") 
# Split the input into a list of phase names
metric_list = metric_str.split(",")
# Validate each input phase against the list of phases
selected_metrics = []
for metric in metric_list:
    metric = metric.strip()
    if metric in all_metrics and metric not in selected_metrics:
        selected_metrics.append(metric)
    else:
        print("Invalid metric: \n", metric)

#Give the option to have bar graph, box plot, or both
#plot_choice = input("Please put what type of plot you would like to have the data represented (Bar Graph, Box Plot, or Both): ")


#Used to get the current working directory of the user
def get_current_directory():
    return os.getcwd()

directory = get_current_directory()

# Define the directory where the report files are stored
reports_dir = directory + '/Reports'

# Use os.listdir() to get a list of all files in the directory
files = os.listdir(reports_dir)

#Creating the bar graphs for the information of specific metrics so that analysis can be performed
import pandas as pd
import matplotlib.pyplot as plt
import os

# Read in all the csv files needed:
# 1. Constraint file
dfc = pd.read_csv("constraints.csv")

# 2. Implement cycling through the csv reports directory
report_csvs = ["Final_Reports.csv", "Cts_Qor_Reports.csv", "Logical_synthesis_Qor_Reports.csv", "Routed_Qor_Reports.csv", "Placed_Qor_Reports.csv"]

if selected_phases == "final":
    report_csvs = "Final_Reports.csv"
elif selected_phases == "placement":
    report_csvs = "Placed_Qor_Reports.csv"
    selected_phases = "placed"
elif selected_phases == "logical_synthesis":
    report_csvs = "Logical_synthesis_Qor_Reports.csv"
elif selected_phases == "cts":
    report_csvs = "Cts_Qor_Reports.csv"
elif selected_phases == "routed":
    report_csvs = "Routed_Qor_Reports.csv"

df = pd.read_csv(report_csvs)
if selected_parameters in ["c_area_effort", "c_map_effort", "in_delay", "out_delay", "s_load", "s_clk_uncert"]: 
    # Filtered contstraints
    filtered_dfc =dfc[dfc[selected_parameters] == selected_parameters_value]
    #print(filtered_dfc)
    filtered_df = df[df['Reports'].str.contains('|'.join(selected_circuits)) & df['Reports'].isin(filtered_dfc['folder'])]
    #print(filtered_df)
else: 
    filtered_df = df[df['Reports'].str.contains('|'.join(selected_circuits))]
    #print(filtered_df)

# Get the number of reports
num_reports = len(filtered_df['Reports'])


if not os.path.exists("ok_metrics"):
    os.mkdir("ok_metrics")

# If the user wants to only evaluate one circuit
if len(selected_circuits) == 1:
    # If the user selects more than 1 metric to evaluate
    if len(selected_metrics) > 1:
        fig, axes = plt.subplots(nrows=len(selected_metrics), ncols=2, figsize=(20, 10))
        for i, metric in enumerate(selected_metrics):  
            # Create bar plot
            ax1 = filtered_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + metric, ax=axes[i][0])
            ax1.tick_params(axis='x', which='major', pad=10)
            ax1.set_xticks(range(num_reports)) # Set the number of x-axis ticks
            labels = ['Test {}'.format(i+1) for i in range(num_reports)] # Create the labels
            ax1.set_xticklabels(labels, fontsize=10) # Set the labels and font size
            ax1.set_title(selected_phases + '_' + metric + ' for ' + circuit)
            ax1.set_xlabel('Reports')
            if metric in ['switching_combinational', 'switching_register', 'total_power']:
                ax1.set_ylabel('uW')
            else:
                ax1.set_ylabel('Values')

            # Create box plot
            ax2 = filtered_df.boxplot(column=selected_phases + '_' + metric, ax=axes[i][1], grid=False)
            ax2.set_title(selected_phases + '_' + metric + ' for ' + circuit)
            if metric in ['switching_combinational', 'switching_register', 'total_power']:
                ax2.set_ylabel('uW')
            else:
                ax2.set_ylabel('Values')
            ax2.tick_params(axis='both', which='major', labelsize=10)
            ax2.set_xticklabels([selected_phases + '_' + metric], fontsize=10)

        plt.subplots_adjust(hspace=1)
        plt.savefig("ok_metrics/ok_metrics.jpg")
        plt.show()

    # If the user only selects 1 metric to evaluate
    elif len(selected_metrics) == 1:
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
        
        # Create bar plot
        ax1 = filtered_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + metric, ax=axes[0])
        ax1.tick_params(axis='x', which='major', pad=10)
        ax1.set_xticks(range(num_reports)) # Set the number of x-axis ticks
        labels = ['Test {}'.format(i+1) for i in range(num_reports)] # Create the labels
        ax1.set_xticklabels(labels, fontsize=10) # Set the labels and font size
        ax1.set_title(selected_phases + '_' + metric + ' for ' + circuit)
        ax1.set_xlabel('Reports')
        if metric in ['switching_combinational', 'switching_register', 'total_power']:
            ax1.set_ylabel('uW')
        else:
            ax1.set_ylabel('Values')

        # Create box plot
        ax2 = filtered_df.boxplot(column=selected_phases + '_' + metric, ax=axes[1], grid=False)
        ax2.set_title(selected_phases + '_' + metric + ' for ' + circuit)
        if metric in ['switching_combinational', 'switching_register', 'total_power']:
            ax2.set_ylabel('uW')
        else:
            ax2.set_ylabel('Values')
        ax2.tick_params(axis='both', which='major', labelsize=10)
        ax2.set_xticklabels([selected_phases + '_' + metric], fontsize=10)

        plt.subplots_adjust(hspace=1)
        plt.savefig("ok_metrics/ok_metrics.jpg")
        plt.show()

# If the user wants to only evaluate more than 1 circuit
elif len(selected_circuits) > 1:
    # If the user selects more than 1 metric to evaluate
    if len(selected_metrics) > 1:
        fig, axes = plt.subplots(nrows=len(selected_metrics), ncols=4, figsize=(20, 10))
        for i, metric in enumerate(selected_metrics):
            circuit1_df = filtered_df[filtered_df['Reports'].str.contains(selected_circuits[0])]
            circuit2_df = filtered_df[filtered_df['Reports'].str.contains(selected_circuits[1])]
            
            # Plot for circuit 1
            ax1 = circuit1_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + metric, ax=axes[i][0])
            ax1.tick_params(axis='x', which='major', pad=10)
            ax1.set_xticks(range(len(circuit1_df))) # Set the number of x-axis ticks
            labels1 = ['Test {}'.format(j+1) for j in range(len(circuit1_df))] # Create the labels
            ax1.set_xticklabels(labels1, fontsize=10) # Set the labels and font size
            ax1.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[0])
            ax1.set_xlabel('Reports')
            if metric in ['switching_combinational', 'switching_register', 'total_power']:
                ax1.set_ylabel('uW')
            else:
                ax1.set_ylabel('Values')
            
            # Plot for circuit 2
            ax2 = circuit2_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + metric, ax=axes[i][1])
            ax2.tick_params(axis='x', which='major', pad=10)
            ax2.set_xticks(range(len(circuit2_df))) # Set the number of x-axis ticks
            labels2 = ['Test {}'.format(j+1) for j in range(len(circuit2_df))] # Create the labels
            ax2.set_xticklabels(labels2, fontsize=10) # Set the labels and font size
            ax2.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[1])
            ax2.set_xlabel('Reports')
            if metric in ['switching_combinational', 'switching_register', 'total_power']:
                ax2.set_ylabel('uW')
            else:
                ax2.set_ylabel('Values')
            
            # Create box plot for circuit 1
            ax3 = circuit1_df.boxplot(column=selected_phases + '_' + metric, ax=axes[i][2], grid=False)
            ax3.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[0])
            if metric in ['switching_combinational', 'switching_register', 'total_power']:
                ax3.set_ylabel('uW')
            else:
                ax3.set_ylabel('Values')
            ax3.tick_params(axis='both', which='major', labelsize=10)
            ax3.set_xticklabels([selected_phases + '_' + metric], fontsize=10)

            # Create box plot for circuit 2
            ax4 = circuit2_df.boxplot(column=selected_phases + '_' + metric, ax=axes[i][3], grid=False)
            ax4.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[1])
            if metric in ['switching_combinational', 'switching_register', 'total_power']:
                ax4.set_ylabel('uW')
            else:
                ax4.set_ylabel('Values')
            ax4.tick_params(axis='both', which='major', labelsize=10)
            ax4.set_xticklabels([selected_phases + '_' + metric], fontsize=10)
                        
            plt.subplots_adjust(wspace=0.4, hspace=1)
            plt.savefig("ok_metrics/{}.jpg".format(metric))
        plt.show()  


    # If the user only selects 1 metric to evaluate
    elif len(selected_metrics) == 1:
        fig, axes = plt.subplots(nrows=len(selected_metrics), ncols=4, figsize=(20, 10))
        circuit1_df = filtered_df[filtered_df['Reports'].str.contains(selected_circuits[0])]
        circuit2_df = filtered_df[filtered_df['Reports'].str.contains(selected_circuits[1])]
            
        # Plot for circuit 1
        ax1 = circuit1_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + metric, ax=axes[0])
        ax1.tick_params(axis='x', which='major', pad=10)
        ax1.set_xticks(range(len(circuit1_df))) # Set the number of x-axis ticks
        labels1 = ['Test {}'.format(j+1) for j in range(len(circuit1_df))] # Create the labels
        ax1.set_xticklabels(labels1, fontsize=10) # Set the labels and font size
        ax1.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[0])
        ax1.set_xlabel('Reports')
        if metric in ['switching_combinational', 'switching_register', 'total_power']:
            ax1.set_ylabel('uW')
        else:
            ax1.set_ylabel('Values')
            
        # Plot for circuit 2
        ax2 = circuit2_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + metric, ax=axes[1])
        ax2.tick_params(axis='x', which='major', pad=10)
        ax2.set_xticks(range(len(circuit2_df))) # Set the number of x-axis ticks
        labels2 = ['Test {}'.format(j+1) for j in range(len(circuit2_df))] # Create the labels
        ax2.set_xticklabels(labels2, fontsize=10) # Set the labels and font size
        ax2.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[1])
        ax2.set_xlabel('Reports')
        if metric in ['switching_combinational', 'switching_register', 'total_power']:
            ax2.set_ylabel('uW')
        else:
            ax2.set_ylabel('Values')
            
        # Create box plot for circuit 1
        ax3 = circuit1_df.boxplot(column=selected_phases + '_' + metric, ax=axes[2], grid=False)
        ax3.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[0])
        if metric in ['switching_combinational', 'switching_register', 'total_power']:
            ax3.set_ylabel('uW')
        else:
            ax3.set_ylabel('Values')
        ax3.tick_params(axis='both', which='major', labelsize=10)
        ax3.set_xticklabels([selected_phases + '_' + metric], fontsize=10)

        # Create box plot for circuit 2
        ax4 = circuit2_df.boxplot(column=selected_phases + '_' + metric, ax=axes[3], grid=False)
        ax4.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[1])
        if metric in ['switching_combinational', 'switching_register', 'total_power']:
            ax4.set_ylabel('uW')
        else:
            ax4.set_ylabel('Values')
        ax4.tick_params(axis='both', which='major', labelsize=10)
        ax4.set_xticklabels([selected_phases + '_' + metric], fontsize=10)
                        
        plt.subplots_adjust(wspace=0.4, hspace=1)
        plt.savefig("ok_metrics/{}.jpg".format(metric))
        plt.show() 

