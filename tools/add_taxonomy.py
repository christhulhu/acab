import os
import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def add_taxonomy(folder_path):
    taxonomy = {
        'class': 'Chilopoda',
        'order': 'Scolopendromorpha',
        'family': 'Scolopendridae',
        'sub_family': 'Scolopendrinae',
        'genus': 'Scolopendra'
    }
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.yml'):
            file_path = os.path.join(folder_path, file_name)
            file_data = read_yaml(file_path)
            file_data['taxonomy'] = taxonomy
            write_yaml(file_path, file_data)

# Verwendung
add_taxonomy('../../data/species')