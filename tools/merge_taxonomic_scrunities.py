import os
import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def process_files(input_file, folder_path):
    input_data = read_yaml(input_file)
    for item in input_data:
        file_name = item['name'].lower().replace(' ', '_') + '.yml'
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            file_data = read_yaml(file_path)
            for key, value in item.items():
                if key not in file_data:
                    file_data[key] = value
                elif key == 'notes':
                    if 'notes' in file_data:
                        file_data['notes'].extend(value)
                    else:
                        file_data['notes'] = value
            write_yaml(file_path, file_data)

# Verwendung
process_files('../../data/scolopendra_species_valid.yml', '../../data/species')
