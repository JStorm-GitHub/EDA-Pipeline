import sys
import csv
import os
import pandas as pd

#Used to get the current working directory of the user

directory = os.getcwd()

# Define the directory where the report files are stored
reports_dir = directory + '/Outputs'
    
# Define the directory where the finalized report files are stored
new_directory = directory + '/Finalized_Reports'


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

def type():
    all_type = ["Synopsys", "Uniform Data Model"] # "OpenRoad"
    print("The following are the types of reports that you can choose from: ", all_type, "\n")
    type_selected = input("Select the type of reports to be analyzed: ")
    return type_selected

def parameter():
    parameters = { "Compile Area Effort": "c_area_effort", "Compile Map Effort": "c_map_effort", "Input Delay": "in_delay",
        "Output Delay": "out_delay", "Set Load": "s_load", "Clock Uncertainty": "s_clk_uncert" }

    parameter_values = { "Compile Area Effort": ["low", "medium", "high"], "Compile Map Effort": ["low", "medium", "high"], "Input Delay": [0.1, 0.5, 1],
        "Output Delay": [0.1, 0.5, 1], "Set Load": [0.2, 0.3], "Clock Uncertainty": [0.05, 0.1] }

    selected_parameter = input("Select the parameter you want to specify, or just hit enter to evaluate all: ")

    if not selected_parameter:
        # Return None if no parameter is selected
        return None, None

    selected_parameter_value = None
    while selected_parameter not in parameters:
        print("Invalid parameter. Please select a valid parameter.")
        selected_parameter = input("Select the parameter you want to specify, or just hit enter to evaluate all: ")

    selected_parameter_value = input(f"Select the value for the {selected_parameter} parameter that you want to evaluate: ")
    if selected_parameter in ["Input Delay", "Output Delay", "Set Load", "Clock Uncertainty"]:
        while True:
            try:
                selected_parameter_value = float(selected_parameter_value)
                if selected_parameter_value in parameter_values[selected_parameter]:
                    break
                else:
                    print("Invalid parameter value. Please enter a valid value.")
                    selected_parameter_value = input(f"Select the value for the {selected_parameter} parameter that you want to evaluate: ")
            except ValueError:
                print("Invalid parameter value. Please enter a numeric value.")
                selected_parameter_value = input(f"Select the value for the {selected_parameter} parameter that you want to evaluate: ")
    elif selected_parameter in ["Compile Area Effort", "Compile Map Effort"]:
        while selected_parameter_value not in parameter_values[selected_parameter]:
            print("Invalid parameter value. Please enter a valid value.")
            selected_parameter_value = input(f"Select the value for the {selected_parameter} parameter that you want to evaluate: ")

    selected_parameter = parameters[selected_parameter]

    return selected_parameter, selected_parameter_value

def circuit():
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
    
    return selected_circuits
        
def phases(type_selected):
    # How to select the phase for the circuit to be evaluated
    if type_selected == "Synopsys":
        all_phases = ["placement", "logical_synthesis", "routed", "cts", "final"]
    #elif type_selected == "OpenRoad":
    #    all_phases = ["placement", "routed", "cts", "final"]
    elif type_selected == "Uniform Data Model":
        all_phases = ["placement", "routed", "cts", "final"]  
    
    print("The following are the phases of circuit(s) that you can choose from: ", all_phases, "\n")
    selected_phases = input("Select the phase that you want to be evaluated: ")


    while selected_phases not in all_phases:
        print ("Invalid phase.\n")
        selected_phases = input("Select the phase(s) that you want to be evaluated: ") #, seperate by a comma if more than 1 (example: placement, final)

    return selected_phases

def get_csv_headers(csv_file, phase_prefix=''):
    df = pd.read_csv(csv_file)
    headers = df.columns.tolist()

    # Exclude specific headers and remove prefix
    excluded_headers = ['Reports']
    excluded_keywords = ['unit']
    headers = [header.replace(phase_prefix, '') for header in headers if header not in excluded_headers and not any(keyword in header for keyword in excluded_keywords)]

    return headers

def metrics(selected_type, selected_phases):
    if selected_type == "Synopsys":
        report_csvs = ["Final_Final_Reports.csv", "Final_cts_Reports.csv", "Final_Logical_Synthesis_Reports.csv", "Final_Routed_Reports.csv", "Final_Placed_Reports.csv"]

        if selected_phases == "final":
            report_csvs = "Final_Final_Reports.csv"
        elif selected_phases == "placement":
            report_csvs = "Final_Placed_Reports.csv"
            selected_phases = "placed"
        elif selected_phases == "logical_synthesis":
            report_csvs = "Final_Logical_Synthesis_Reports.csv"
        elif selected_phases == "cts":
            report_csvs = "Final_cts_Reports.csv"
        elif selected_phases == "routed":
            report_csvs = "Final_Routed_Reports.csv"
            
    #elif selected_type == "OpenRoad":
    #    report_csvs = ["cts_reports.csv", "final_reports.csv", "placement_reports.csv", "routing_reports.csv"]
    #    
    #    if selected_phases == "final":
    #        report_csvs = "final_reports.csv"
    #        selected_phases == "finish"
    #    elif selected_phases == "placement":
    #        report_csvs = "placement_reports.csv"
    #        selected_phases == "globalplace"
    #    elif selected_phases == "cts":
    #        report_csvs = "cts_reports.csv"
    #    elif selected_phases == "routed":
    #        report_csvs = "routing_reports.csv"
    #        selected_phases == "globalroute"
            
    elif selected_type == "Uniform Data Model":
        if selected_phases == "cts":
            report_csvs = "cts_udm.csv"
    
    # If report_csvs is a list, select the first one
    if isinstance(report_csvs, list):
        csv_file = os.path.join(new_directory, report_csvs[0])
    else:
        csv_file = os.path.join(new_directory, report_csvs)
    
    selected_metrics = []
    
    if os.path.exists(csv_file):
        headers = get_csv_headers(csv_file)
        
        excluded_headers = ['Reports', 'Unnamed: 0']
        
        # Remove the selected phase prefix from metric headers
        headers = [header.replace(selected_phases + '_', '') for header in headers if header not in excluded_headers]

        print("The following are the metrics of circuit(s) that you can choose from: ", headers, "\n")
        metric_str = input("Select the metric(s) that you want to be evaluated, separated by a comma if more than 1 (example: design_area, other_metric): ")
        # Split the input into a list of metric names
        metric_list = metric_str.split(",")
        # Validate each input metric against the list of headers
        for metric in metric_list:
            metric = metric.strip()
            if metric in headers and metric not in selected_metrics:
                selected_metrics.append(metric)
            else:
                print("Invalid metric: \n", metric)
    else:
        print("Selected CSV file does not exist.")

    return selected_metrics




def plot(selected_type, selected_parameters, selected_parameters_value, selected_circuits, selected_phases, selected_metrics):
    
    # Options of plots to choose from
    all_plots = ["Bar Graph", "Box Plot"]
    print("The following are the types of graphs that you can choose from: ", all_plots, "\n")
    plot_str = input("Select the type of graph(s) that you would like created, seperate by a comma if more than 1 (example: Bar Graph, Box Plot): ") 
    # Split the input into a list of phase names
    plot_list = plot_str.split(",")
    # Validate each input phase against the list of phases
    selected_plots = []
    for plot in plot_list:
        plot = plot.strip()
        if plot in all_plots and plot not in selected_plots:
            selected_plots.append(plot)
        else:
            print("Invalid graph type: \n", plot)
    
    import os

    # Use os.listdir() to get a list of all files in the directory
    files = os.listdir(reports_dir)

    #Creating the bar graphs for the information of specific metrics so that analysis can be performed
    import matplotlib.pyplot as plt
    import os

    # Read in all the csv files needed:
    # 1. Constraint file
    dfc = pd.read_csv(os.path.join(new_directory, "constraints.csv"))

    if selected_type == "Synopsys":
        # 2. Implement cycling through the csv reports directory
        report_csvs = ["Final_Final_Reports.csv", "Final_cts_Reports.csv", "Final_Logical_Synthesis_Reports.csv", "Final_Routed_Reports.csv", "Final_Placed_Reports.csv"]

        if selected_phases == "final":
            report_csvs = "Final_Final_Reports.csv"
        elif selected_phases == "placement":
            report_csvs = "Final_Placed_Reports.csv"
            selected_phases = "placed"
        elif selected_phases == "logical_synthesis":
            report_csvs = "Final_Logical_Synthesis_Reports.csv"
        elif selected_phases == "cts":
            report_csvs = "Final_cts_Reports.csv"
        elif selected_phases == "routed":
            report_csvs = "Final_Routed_Reports.csv"
            
    #elif selected_type == "OpenRoad":
    #    report_csvs = ["cts_reports.csv", "final_reports.csv", "placement_reports.csv", "routing_reports.csv"]
    #    
    #    if selected_phases == "final":
    #        report_csvs = "final_reports.csv"
    #    elif selected_phases == "placement":
    #        report_csvs = "placement_reports.csv"
    #        selected_phases = "placed"
    #    elif selected_phases == "cts":
    #        report_csvs = "cts_reports.csv"
    #    elif selected_phases == "routed":
    #        report_csvs = "routing_reports.csv"
            
    elif selected_type == "Uniform Data Model":
        if selected_phases == "cts":
            report_csvs = "cts_udm.csv"
        
            
        
    df = pd.read_csv(os.path.join(new_directory, report_csvs))

    if selected_parameters is not None:
        if selected_parameters in ["c_area_effort", "c_map_effort", "in_delay", "out_delay", "s_load", "s_clk_uncert"]:
            # Filtered constraints
            filtered_dfc = dfc[dfc[selected_parameters] == selected_parameters_value]
            filtered_df = df[df['Reports'].str.contains('|'.join(selected_circuits)) & df['Reports'].isin(filtered_dfc['folder'])]
        else:
            filtered_df = df[df['Reports'].str.contains('|'.join(selected_circuits))]
    else:
        filtered_df = df[df['Reports'].str.contains('|'.join(selected_circuits))]


    # Get the number of reports
    num_reports = len(filtered_df['Reports'])

    if not os.path.exists("Graphs_Plots"):
        os.mkdir("Graphs_Plots")
        
    i = 0
    while i < len(selected_plots):
        if selected_plots[i] == "Bar Graph":
            # If the user wants to only evaluate one circuit and one metric
            if len(selected_circuits) == 1 and len(selected_metrics) == 1:
                circuit_df = filtered_df[filtered_df['Reports'].str.contains(selected_circuits[0])]
                fig, ax = plt.subplots(figsize=(10, 5))
                ax = circuit_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + selected_metrics[0], ax=ax)
                ax.tick_params(axis='x', which='major', pad=10)
                ax.set_xticks(range(len(circuit_df))) # Set the number of x-axis ticks
                labels = ['Test {}'.format(j+1) for j in range(len(circuit_df))] # Create the labels
                ax.set_xticklabels(labels, fontsize=10) # Set the labels and font size
                ax.set_title(selected_phases + '_' + selected_metrics[0] + ' for ' + selected_circuits[0])
                ax.set_xlabel('Reports')
                if selected_metrics[0] in ['switching_combinational', 'switching_register', 'total_power']:
                    ax.set_ylabel('uW')
                elif any(m in metric for m in ["tns", "ws"]):
                    ax.set_ylabel('ps')
                else:
                    ax.set_ylabel('Values')
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.savefig('Graphs_Plots/{}_{}_bar_graph.png'.format(selected_phases, selected_metrics[0]))
                plt.show()
                
            # If the user selects more than 1 circuit and only 1 metric
            elif len(selected_circuits) > 1 and len(selected_metrics) == 1:
                fig, axes = plt.subplots(nrows=len(selected_circuits), ncols=1, figsize=(10, 5*len(selected_circuits)))
                for i, circuit in enumerate(selected_circuits):
                    # Create bar plot for each circuit and one metric
                    circuit_df = filtered_df[filtered_df['Reports'].str.contains(circuit)]
                    ax = circuit_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + selected_metrics[0], ax=axes[i])
                    ax.tick_params(axis='x', which='major', pad=10)
                    ax.set_xticks(range(len(circuit_df))) # Set the number of x-axis ticks
                    labels = ['Test {}'.format(j+1) for j in range(len(circuit_df))] # Create the labels
                    ax.set_xticklabels(labels, fontsize=10) # Set the labels and font size
                    ax.set_title(selected_phases + '_' + selected_metrics[0] + ' for ' + circuit)
                    ax.set_xlabel('Reports')
                    if selected_metrics[0] in ['switching_combinational', 'switching_register', 'total_power']:
                        ax.set_ylabel('uW')
                    elif any(m in metric for m in ["tns", "ws"]):
                        ax.set_ylabel('ps')
                    else:
                        ax.set_ylabel('Values')
                    plt.xticks(rotation=90)
                    plt.tight_layout()
                    plt.savefig('Graphs_Plots/{}_{}_bar_graph.png'.format(selected_phases, selected_metrics[0]))
                plt.show()
            
            # If the user selects only 1 circuit and more than 1 metric
            elif len(selected_circuits) == 1 and len(selected_metrics) > 1:
                fig, axes = plt.subplots(nrows=len(selected_metrics), ncols=1, figsize=(10, 5*len(selected_metrics)))
                for i, metric in enumerate(selected_metrics):
                    # Create bar plot for one circuit and each selected metric
                    ax = filtered_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + metric, ax=axes[i])
                    ax.tick_params(axis='x', which='major', pad=10)
                    ax.set_xticks(range(num_reports)) # Set the number of x-axis ticks
                    labels = ['Test {}'.format(i+1) for i in range(num_reports)] # Create the labels
                    ax.set_xticklabels(labels, fontsize=10) # Set the labels and font size
                    ax.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[0])
                    ax.set_xlabel('Reports')
                    if metric in ['switching_combinational', 'switching_register', 'total_power']:
                        ax.set_ylabel('uW')
                    elif any(m in metric for m in ["tns", "ws"]):
                        ax.set_ylabel('ps')
                    else:
                        ax.set_ylabel('Values')
                    plt.xticks(rotation=90)
                    plt.tight_layout()
                    plt.savefig('Graphs_Plots/{}_{}_bar_graph.png'.format(selected_phases, metric))
                plt.show()

            # If the user selects more than 1 circuit and more than 1 metric
            elif len(selected_circuits) > 1 and len(selected_metrics) > 1:
                fig, axes = plt.subplots(nrows=len(selected_metrics), ncols=len(selected_circuits), figsize=(5*len(selected_circuits), 5*len(selected_metrics)))
                for i, metric in enumerate(selected_metrics):
                    for j, circuit in enumerate(selected_circuits):
                        circuit_df = filtered_df[filtered_df['Reports'].str.contains(circuit)]
                        ax = circuit_df.plot(kind='bar', x='Reports', y=selected_phases + '_' + metric, ax=axes[i,j])
                        ax.tick_params(axis='x', which='major', pad=10)
                        ax.set_xticks(range(len(circuit_df))) # Set the number of x-axis ticks
                        labels = ['Test {}'.format(k+1) for k in range(len(circuit_df))] # Create the labels
                        ax.set_xticklabels(labels, fontsize=10) # Set the labels and font size
                        ax.set_title(selected_phases + '_' + metric + ' for ' + circuit)
                        ax.set_xlabel('Reports')
                        if metric in ['switching_combinational', 'switching_register', 'total_power']:
                            ax.set_ylabel('uW')
                        elif any(m in metric for m in ["tns", "ws"]):
                            ax.set_ylabel('ps')
                        else:
                            ax.set_ylabel('Values')
                plt.tight_layout()
                plt.savefig('Graphs_Plots/{}_{}_bar_graph.png'.format(selected_phases, metric))
                plt.show()

        elif selected_plots[i] == "Box Plot":
            # If the user wants to only evaluate one circuit and one metric
            if len(selected_circuits) == 1 and len(selected_metrics) == 1:
                circuit_df = filtered_df[filtered_df['Reports'].str.contains(selected_circuits[0])]
                fig, ax = plt.subplots(figsize=(10, 5))
                ax = circuit_df.boxplot(column=selected_phases + '_' + selected_metrics[0], ax=ax, grid=False)
                ax.set_title(selected_phases + '_' + selected_metrics[0] + ' for ' + selected_circuits[0])
                if selected_metrics[0] in ['switching_combinational', 'switching_register', 'total_power']:
                    ax.set_ylabel('uW')
                elif any(m in metric for m in ["tns", "ws"]):
                    ax.set_ylabel('ps')
                else:
                    ax.set_ylabel('Values')
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.savefig('Graphs_Plots/{}_{}_box_plot.png'.format(selected_phases, selected_metrics[0]))
                plt.show()

            # If the user selects more than 1 circuit and only 1 metric
            elif len(selected_circuits) > 1 and len(selected_metrics) == 1:
                fig, axes = plt.subplots(nrows=len(selected_circuits), ncols=1, figsize=(10, 5*len(selected_circuits)))
                for i, circuit in enumerate(selected_circuits):
                    # Create box plot for each circuit and one metric
                    circuit_df = filtered_df[filtered_df['Reports'].str.contains(circuit)]
                    ax = circuit_df.boxplot(column=selected_phases + '_' + selected_metrics[0], ax=axes[i], grid=False)
                    ax.set_title(selected_phases + '_' + selected_metrics[0] + ' for ' + circuit)
                    ax.set_xlabel('Circuit')
                    if selected_metrics[0] in ['switching_combinational', 'switching_register', 'total_power']:
                        ax.set_ylabel('uW')
                    elif any(m in metric for m in ["tns", "ws"]):
                        ax.set_ylabel('ps')
                    else:
                        ax.set_ylabel('Values')
                    plt.xticks(rotation=90)
                    plt.tight_layout()
                    plt.savefig('Graphs_Plots/{}_{}_box_plot.png'.format(selected_phases, selected_metrics[0]))
                plt.show()

            # If the user selects only 1 circuit and more than 1 metric
            elif len(selected_circuits) == 1 and len(selected_metrics) > 1:
                fig, axes = plt.subplots(nrows=len(selected_metrics), ncols=1, figsize=(10, 5*len(selected_metrics)))
                for i, metric in enumerate(selected_metrics):
                    # Create box plot for one circuit and each selected metric
                    ax = filtered_df.boxplot(column=selected_phases + '_' + metric, ax=axes[i], grid=False)
                    ax.set_title(selected_phases + '_' + metric + ' for ' + selected_circuits[0])
                    ax.set_xlabel('Circuit')
                    if metric in ['switching_combinational', 'switching_register', 'total_power']:
                        ax.set_ylabel('uW')
                    elif any(m in metric for m in ["tns", "ws"]):
                        ax.set_ylabel('ps')
                    else:
                        ax.set_ylabel('Values')
                    plt.xticks(rotation=90)
                    plt.tight_layout()
                    plt.savefig('Graphs_Plots/{}_{}_box_plot.png'.format(selected_phases, metric))
                plt.show()

            # If the user selects more than 1 circuit and more than 1 metric
            elif len(selected_circuits) > 1 and len(selected_metrics) > 1:
                fig, axes = plt.subplots(nrows=len(selected_metrics), ncols=len(selected_circuits), figsize=(5*len(selected_circuits), 5*len(selected_metrics)))
                for i, metric in enumerate(selected_metrics):
                    for j, circuit in enumerate(selected_circuits):
                        circuit_df = filtered_df[filtered_df['Reports'].str.contains(circuit)]
                        ax = circuit_df.boxplot(column=selected_phases + '_' + metric, ax=axes[i, j], grid=False)
                        ax.set_title(selected_phases + '_' + metric + ' for ' + circuit)
                        ax.set_xlabel('Circuit')
                        if metric in ['switching_combinational', 'switching_register', 'total_power']:
                            ax.set_ylabel('uW')
                        elif any(m in metric for m in ["tns", "ws"]):
                            ax.set_ylabel('ps')
                        else:
                            ax.set_ylabel('Values')
                plt.tight_layout()
                plt.savefig('Graphs_Plots/{}_{}_box_plot.png'.format(selected_phases, metric))
                plt.show()
                         
        elif selected_plots[i] == "All":
            #Make All
            print ("Done")

        i = i + 1
        

def main():
    type_selected = type()
    selected_phases = phases(type_selected)
    selected_parameters, selected_parameters_value = parameter()
    circuits_selected = circuit()
    selected_metrics = metrics(type_selected, selected_phases)
    
    plot(type_selected, selected_parameters, selected_parameters_value, circuits_selected, selected_phases, selected_metrics)


main()
