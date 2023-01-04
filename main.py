# Open the file containing the interface information
filepath = "\interfaces.txt"
with open(filepath, 'r') as f:
    # Read the lines of the file and store them in a list
    interface_list = f.readlines()

# Filter the list to only include lines that do not contain the word "down"
filtered_list = [item for item in interface_list if "down" not in item]

# Filter the list to remove blank lines
filtered_list = [line for line in filtered_list if line.strip()]

# Initialize an empty list to store the commands
commands = []

# Iterate through each line in the filtered list
for line in filtered_list:
    # Extract the interface name from the line
    interface = line.split()[1].split('.')[0]
    # Add the commands for the interface to the list
    commands.extend([f'interface gi {interface}', 'shut', 'no shut'])

# Open the output file
with open('output.txt', 'w') as f:
    # Write each command to the file, followed by a newline character
    for command in commands:
        f.write(f"{command}\n")
