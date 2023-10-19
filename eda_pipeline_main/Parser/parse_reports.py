import re
import openpyxl
import os
import json
import csv
import shutil


##example
##desing_name = s386
##variant_dir = synopsys_s386_2
#for n in range(i):
#    design_variant = f"{design_name}_{n}"    #the name of the compilation run
#    file = f"synopsys_{design_variant}"    #the directory containing this run
#    work_home = os.path.join(output_dir, variant_dir)    #full path for outputted variant directory
#    os.chdir(work_home)


def clear_directory(directory_path):
    shutil.rmtree(directory_path)

def parse_qor_report(report_path1):
    """Parse Synopsys ICC QOR reports
    Parameters
    ----------
    report_path : str
        QOR report file path
    Returns
    ----------
    dict
        Parsed QOR metrics
    """
    with open(report_path1) as fp:
        txt = fp.read()
    txt = txt.split("Report : qor")[-1]

    data1 = []
    for k, v in re.findall(r"([^0-9|\n]+?):\s+([0-9|\.|\-]+?)\n", txt):
        k = re.sub(r"\s+", " ", k)
        k = k.replace(" ", "_").lower()
        k = re.sub("[^a-z|_]", "", k)
        if "-" in v:
            v = str(abs(float(v)))
        data1.append((phase + k, v))


    return dict(sorted(data1))


def parse_power_report(report_path2):
    """Parse Synopsys ICC power reports
    Parameters
    ----------
    report_path : str
        Power report file path
    Returns
    ----------
    dict
        Parsed power metrics
    """
    with open(report_path2) as fp:
        txt = fp.read()

    split_list = txt.split("-" * 98)
    power_txt = split_list[1]
    total_txt = split_list[2]

    internal_unit, switching_unit, leakage_unit, total_unit = re.findall(
        r" ([a-z]W)", total_txt
    )
    data_dict = {
        "internal_unit": internal_unit,
        "switching_unit": switching_unit,
        "leakage_unit": leakage_unit,
    }

    regex = r"([a-z|_]+)\s+([0-9|\.|e|-]+)\s+([0-9|\.|e|-]+)\s+([0-9|\.|e|-]+)"
    for power_group, internal, switching, leakage in re.findall(regex, power_txt):
        data_dict["internal_" + power_group] = internal
        data_dict["switching_" + power_group] = switching
        data_dict["leakage_" + power_group] = leakage

    regex = r"\s+([0-9|\.|e|-]+) ([a-z]W)\n"
    total_power, total_power_unit = re.findall(regex, total_txt)[0]
    data_dict["total_power"] = total_power
    data_dict["total_power_unit"] = total_power_unit

    data2 = []
    for k, v in data_dict.items():
        data2.append((phase + "_" + k, v))
        


    return dict(sorted(data2))


def read_timing_report(report_path3):
    txt = ""
    #for i in range(1, 5):
        #report_path = "{}/pt_post/reports/{}_timing_{}.rpt".format(file_path, phase, i)
    with open(report_path3) as fp:
        txt += fp.read()
    return txt


def parse_timing_path(path_str):
    path_info = []
    for line in re.findall("[a-z|A-Z].*?\n", path_str):
        line = line.replace("<-", "")
        point_match = re.findall(r"^(.*?) \((.*?)\)  ", line) or re.findall(
            r"^(.*?) () ", line
        )
        node_name, node_info = point_match[0]
        if node_name == "data required time":
            break
        node_name = node_name.replace("_snps_wire", "")

        values = re.findall(r" ([0-9|\.|-]+?)[ |\n]", line)
        if node_info == "net":
            delay_info = [node_name, node_info, int(values[-2]), float(values[-1])]
        else:
            delay_info = [
                node_name,
                node_info,
                float(values[-2]) if len(values) > 1 else 0.0,
                float(values[-1]),
            ]
        path_info.append(delay_info)

    arrival_time_path, required_time_path = [], []
    parsing_arrival_time = True
    for node_name, node_info, node_delay, path_delay in path_info:
        if node_name == "data arrival time":
            parsing_arrival_time = False
            continue
        if parsing_arrival_time:
            arrival_time_path.append([node_name, node_info, node_delay, path_delay])
        else:
            required_time_path.append([node_name, node_info, node_delay, path_delay])

    return arrival_time_path, required_time_path


def parse_timing_report(file_path, phase):
    """Parse Synopsys ICC/PrimeTime timing reports
    Parameters
    ----------
    file_path : str
        Base directory for physical design
    phase : str
        EDA [hase
    Returns
    ----------
    dict
        Parsed timing report with slack values and arrival times
    """
    report_path3 = os.getcwd()
    txt = read_timing_report(report_path3)
    data_dict = {}
    for match_str in re.findall(r"Startpoint.*?slack.*?\n", txt, re.DOTALL):
        path_info_dict = dict(re.findall(r"\s*(.+?): (.+?)\n", match_str))
        startpoint = path_info_dict["Startpoint"].split(" ")[0]
        endpoint = path_info_dict["Endpoint"].split(" ")[0]

        path_str = re.findall("Path\n(.*)", match_str, re.DOTALL)[0]
        
        parse_timing_path(path_str)
        
        arrival_time_path, required_time_path = parse_timing_path(path_str)
        slack = float(re.findall(r"slack.*?([0-9|\.|-]+?)\n", match_str)[0])

        data_dict[(startpoint, endpoint)] = {
            "arrival_time_path": arrival_time_path,
            "required_time_path": required_time_path,
            "slack": slack,
        }

def extract_headers(json_data):
    headers = []
    for key in json_data.keys():
        headers.append(key)
    return headers

def process_phase_reports(json_files, phase_prefix, csv_file):
    temp_json_file = 'temp.json'

    # Combine JSON files into a temporary JSON
    combined_data = {}
    for json_file in json_files:
        json_path = os.path.join(report_list_path, json_file)
        with open(json_path) as file:
            json_data = json.load(file)
            combined_data.update(json_data)

    # Write combined data to temporary JSON
    with open(temp_json_file, 'w') as file:
        json.dump(combined_data, file)

    # Convert temporary JSON to CSV
    with open(temp_json_file) as file:
        json_data = json.load(file)
        with open(csv_file, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            if csv_file.tell() == 0:
                # Write headers if it's the first entry
                headers = list(json_data.keys())
                writer.writerow(headers)
            row_data = []
            for value in json_data.values():
                # Take the absolute value of a specific value
                if isinstance(value, (int, float)):
                    value = abs(value)
                row_data.append(value)
            writer.writerow(row_data)

    # Delete temporary JSON file
    os.remove(temp_json_file)

#Used to get the current working directory of the user
def get_current_directory():
    return os.getcwd()

directory = get_current_directory()

if os.path.exists('Finalized_Reports'):
    clear_directory(os.path.join(os.getcwd(), 'Finalized_Reports'))

# Create new directory/folder to save reports into 
new_directory = os.path.join(directory, 'Finalized_Reports')

if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# Define the directory where the report files are stored
reports_dir =os.path.join(directory + '/Outputs')


# Use os.listdir() to get a list of all files in the directory
files = os.listdir(reports_dir)
#print(files)

qor_final_data = []
qor_cts_data = []
qor_logical_synthesis_data = []
qor_placed_data = []
qor_routed_data = []
power_final_data = []
power_logical_synthesis_data = []
power_cts_data = []
power_routed_data = []
power_placed_data = []

# Initialize report dictionaries
qor_final_report_dict = {}
power_final_report_dict = {}
qor_logical_synthesis_report_dict = {}
qor_cts_report_dict = {}
qor_routed_report_dict = {}
qor_placed_report_dict = {}
power_logical_synthesis_report_dict = {}
power_cts_report_dict = {}
power_routed_report_dict = {}
power_placed_report_dict = {}


for file in files:
    pattern = r'[a-zA-Z]\d'

    # Check if any folder in the iteration contains the pattern "s" followed by a series of numbers
    if not any(
        re.search(r's\d+', folder) for folder in os.listdir(reports_dir + "/" + file) if folder != ".gitkeep"
    ):
        continue  # Move to the next iteration if the condition is not met
    # Rest of your code...
    circuit = re.search(r'[a-z]\d+', file).group(0)
    #print(circuit)
    
    
    if any("synopsys" in file for files in files):
        # Code used to generate the reports in the final phase
        #print("syn")
           
        phase = "final"
                
        report_path1 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_" + phase + "_qor.rpt"
        report_path2 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_" + phase +  "_power.rpt"

        qor_final_report_dict = parse_qor_report(report_path1)
        power_final_report_dict = parse_power_report(report_path2)
            
        # Code used to generate the reports in the logical synthesis phase
        phase = 'logical_synthesis'
                
        report_path1 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_dcc_qor.rpt"
        report_path2 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_dcc_power.rpt"
                   
        qor_logical_synthesis_report_dict = parse_qor_report(report_path1)
        power_logical_synthesis_report_dict = parse_power_report(report_path2)
        

        # CTS Reports
        phase = 'cts'

        report_path1 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_" + phase + "_qor.rpt"
        report_path2 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_" + phase + "_power.rpt"

        
        qor_cts_report_dict = parse_qor_report(report_path1)
        power_cts_report_dict = parse_power_report(report_path2)

        # Routed Reports
        phase = 'routed'

        report_path1 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_route_qor.rpt"
        report_path2 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_route_power.rpt"
    
        qor_routed_report_dict = parse_qor_report(report_path1)
        power_routed_report_dict = parse_power_report(report_path2)

        # Floorplan Reports
        # Skipping for now

        # Placed Reports
        phase = 'placed'
        report_path1 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_place_qor.rpt"
        report_path2 = reports_dir + "/" + file + "/" + phase + "/reports/" + circuit + "_place_power.rpt"
     
        qor_placed_report_dict = parse_qor_report(report_path1)
        power_placed_report_dict = parse_power_report(report_path2)
        
        #Append the data from the parsed reports and add them to the csv file
        qor_final_data.append(list(qor_final_report_dict.values()))
        qor_logical_synthesis_data.append(list(qor_logical_synthesis_report_dict.values()))
        qor_cts_data.append(list(qor_cts_report_dict.values()))
        qor_routed_data.append(list(qor_routed_report_dict.values()))
        qor_placed_data.append(list(qor_placed_report_dict.values()))
        power_final_data.append(list(power_final_report_dict.values()))
        power_logical_synthesis_data.append(list(power_logical_synthesis_report_dict.values()))
        power_cts_data.append(list(power_cts_report_dict.values()))
        power_routed_data.append(list(power_routed_report_dict.values()))
        power_placed_data.append(list(power_placed_report_dict.values()))
        
    if any("openroad" in file for files in files):
        
        circuit_follower = file[len('openroad_'):]
        report_list_path = os.path.join(reports_dir, file, 'logs', 'sky130hd', circuit, circuit_follower)
        json_files = [f for f in os.listdir(report_list_path) if f.endswith('.json')]

        if any(file_name.startswith('3_') for file_name in json_files):
            placement_csv_file = os.path.join(new_directory, 'placement_reports.csv')
            placement_json_files = [f for f in json_files if f.startswith('3_')]
            process_phase_reports(placement_json_files, '3_', placement_csv_file)

        if any(file_name.startswith('4_') for file_name in json_files):
            cts_csv_file = os.path.join(new_directory, 'cts_reports.csv')
            cts_json_files = [f for f in json_files if f.startswith('4_')]
            process_phase_reports(cts_json_files, '4_', cts_csv_file)

        if any(file_name.startswith('5_') for file_name in json_files):
            routing_csv_file = os.path.join(new_directory, 'routing_reports.csv')
            routing_json_files = [f for f in json_files if f.startswith('5_')]
            process_phase_reports(routing_json_files, '5_', routing_csv_file)
            
        if any(file_name.startswith('6_') for file_name in json_files):
            final_csv_file = os.path.join(new_directory, 'final_reports.csv')
            final_json_files = [f for f in json_files if f.startswith('6_')]
            process_phase_reports(final_json_files, '6_', final_csv_file)


#Get the headers for each column and add them to the csv file
qor_final_headers = list(qor_final_report_dict.keys())
qor_logical_synthesis_headers = list(qor_logical_synthesis_report_dict.keys())
qor_cts_headers = list(qor_cts_report_dict.keys())
qor_routed_headers = list(qor_routed_report_dict.keys())
qor_placed_headers = list(qor_placed_report_dict.keys())
power_final_headers = list(power_final_report_dict.keys())
power_logical_synthesis_headers = list(power_logical_synthesis_report_dict.keys())
power_cts_headers = list(power_cts_report_dict.keys())
power_routed_headers = list(power_routed_report_dict.keys())
power_placed_headers = list(power_placed_report_dict.keys())



#Process of creating the csv file for the combined reports and writing the headers and data to it
import pandas as pd
import csv

with open(os.path.join(new_directory, "Final_Final_Reports.csv"), "w", newline="") as file:
    writer = csv.writer(file)
    final_headers = qor_final_headers + power_final_headers
    writer.writerow(final_headers)
    for i in range(len(qor_final_data)):
        writer.writerow(qor_final_data[i] + power_final_data[i])
        
with open(os.path.join(new_directory, "Final_cts_Reports.csv"), "w", newline="") as file:
    writer = csv.writer(file)
    final_headers = qor_cts_headers + power_cts_headers
    writer.writerow(final_headers)
    for i in range(len(qor_cts_data)):
        writer.writerow(qor_cts_data[i] + power_cts_data[i])
        
with open(os.path.join(new_directory, "Final_Logical_Synthesis_Reports.csv"), "w", newline="") as file:
    writer = csv.writer(file)
    final_headers = qor_logical_synthesis_headers + power_logical_synthesis_headers
    writer.writerow(final_headers)
    for i in range(len(qor_logical_synthesis_data)):
        writer.writerow(qor_logical_synthesis_data[i] + power_logical_synthesis_data[i])
        
with open(os.path.join(new_directory, "Final_Routed_Reports.csv"), "w", newline="") as file:
    writer = csv.writer(file)
    final_headers = qor_routed_headers + power_routed_headers
    writer.writerow(final_headers)
    for i in range(len(qor_routed_data)):
        writer.writerow(qor_routed_data[i] + power_routed_data[i])
        
with open(os.path.join(new_directory, "Final_Placed_Reports.csv"), "w", newline="") as file:
    writer = csv.writer(file)
    final_headers = qor_placed_headers + power_placed_headers
    writer.writerow(final_headers)
    for i in range(len(qor_placed_data)):
        writer.writerow(qor_placed_data[i] + power_placed_data[i])
    
synopsys_reports = ["Final_Final_Reports.csv", "Final_cts_Reports.csv", "Final_Logical_Synthesis_Reports.csv", "Final_Routed_Reports.csv", "Final_Placed_Reports.csv"]
openroad_reports = ["cts_reports.csv", "final_reports.csv", "placement_reports.csv", "routing_reports.csv"]

synopsys_files = [file for file in files if 'synopsys' in file]
synopsys_files.sort()

openroad_files = [file for file in files if 'openroad' in file]
openroad_files.sort()

# Process Synopsys reports
for report in synopsys_reports:
    report_path = os.path.join(new_directory, report)
    df = pd.read_csv(report_path)
    new_column_name = 'Reports'
    if new_column_name not in df.columns:
        df.insert(0, new_column_name, synopsys_files)
        df.to_csv(report_path, index=False)

# Process Openroad reports
for report in openroad_reports:
    report_path = os.path.join(new_directory, report)
    df = pd.read_csv(report_path)
    new_column_name = 'Reports'
    if new_column_name not in df.columns:
        df.insert(0, new_column_name, openroad_files)
        df.to_csv(report_path, index=False)

# Combining the cts phases of synopsys and openroad into a uniform data model
df1 = pd.read_csv(os.path.join(new_directory, 'cts_reports.csv'))
df2 = pd.read_csv(os.path.join(new_directory, 'Final_cts_Reports.csv'))

# Select the desired metrics from each DataFrame
metrics_df1 = df1[['Reports', 'cts__timing__setup__tns', 'cts__timing__setup__ws']]
metrics_df2 = df2[['Reports', 'cts_total_hold_violation', 'cts_worst_hold_violation']]

# Rename the columns
metrics_df1 = metrics_df1.rename(columns={'cts__timing__setup__tns': 'cts_combined_tns', 'cts__timing__setup__ws': 'cts_combined_ws'})
metrics_df2 = metrics_df2.rename(columns={'cts_total_hold_violation': 'cts_combined_tns', 'cts_worst_hold_violation': 'cts_combined_ws'})

# Combine the metrics into a single DataFrame
combined_metrics = pd.concat([metrics_df1, metrics_df2]).reset_index(drop=True)

# Create the merged DataFrame
merged = combined_metrics.dropna(subset=['Reports'])

merged.to_csv(os.path.join(new_directory, 'cts_udm.csv'))
#print(merged)






















# Create a list to hold the extracted constraints
constraints = []

# Loop through each folder
for folder in synopsys_files:
    folder_path = os.path.join(reports_dir, folder)
    # Check if the folder contains a text file with the phrase "config"
    if any('config' in file for file in os.listdir(folder_path)):
        # Extract the constraints from the text file
        constraint_dict = {}
        for file in os.listdir(folder_path):
            if 'config' in file:
                with open(os.path.join(folder_path, file), 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith('set'):
                            key, value = line.strip().split()[1:]
                            constraint_dict[key] = value
        constraint_dict['folder'] = folder
        constraints.append(constraint_dict)

# Write the constraints to a CSV file
with open(os.path.join(new_directory, 'constraints.csv'), 'w', newline='') as csvfile:
    fieldnames = ['folder', 'file_name', 'c_area_effort', 'c_map_effort', 'in_delay', 'out_delay', 's_load', 's_clk_uncert']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for constraint in constraints:
        # Filter out any fields not present in fieldnames
        filtered_constraint = {key: constraint.get(key, '') for key in fieldnames}
        writer.writerow(filtered_constraint)


