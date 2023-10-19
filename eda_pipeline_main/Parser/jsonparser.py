import json
import os

# this just makes the current directory you're in the working directory
directory_path = os.getcwd()

# This is the loop to go through every json file
for filename in os.listdir(directory_path):
    if filename.endswith('.json'):

        # opening the json file to manipulate data inside it
        with open(os.path.join(directory_path, filename), 'r') as json_file:
            data = json.load(json_file)

        # another loop to go through each line and split the lines into two objects
        for line in data:
            split_line = line.split(';')
            if len(split_line) == 2:

                # This changes the value part of the line into an integer
                split_line[1] = int(split_line[1].strip())
                data.append({'description': split_line[0], 'value': split_line[1]})
        
        # this sends the newly modified data right back into the original json file we opened and manipulated
        with open(os.path.join(directory_path, filename), 'w') as json_file:
            json.dump(data, json_file, indent=4)

