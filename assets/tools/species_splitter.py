import yaml
import os

def create_files_from_yaml(yaml_file, output_dir):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for entry in data:
        filename = os.path.join(output_dir, entry['name'].lower().replace(' ', '_') + '.yml')
        if not os.path.exists(filename):
            with open(filename, 'w') as new_file:
                new_file.write(f"name: {entry['name']}\n")
                new_file.write(f"first_description: {entry['first_description']}\n")

# Verwendung
create_files_from_yaml('/home/christian/code/prvt/scolohub.com/data/scolopendra_species_valid.yml', '/home/christian/code/prvt/scolohub.com/data/species/')