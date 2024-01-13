import os
import yaml

def create_md_files(src_folder, dest_folder):
    for filename in os.listdir(src_folder):
        if filename.endswith('.yml'):
            with open(os.path.join(src_folder, filename), 'r') as file:
                data = yaml.safe_load(file)
                if 'name' in data:
                    new_folder_name = filename.split('_')[-1].replace('.yml', '')
                    new_folder = os.path.join(dest_folder, new_folder_name)
                    os.makedirs(new_folder, exist_ok=True)
                    with open(os.path.join(new_folder, 'index.md'), 'w') as md_file:
                        md_file.write('---\n')
                        md_file.write('title: ' + data['name'] + '\n')
                        md_file.write('description: Die Art ' + data['name'] + '\n')
                        md_file.write('bookHidden: true\n')
                        md_file.write('type: page\n')
                        md_file.write('layout: taxonomy_species\n')
                        md_file.write('datafile: ' + filename.replace('.yml', '') + '\n')
                        md_file.write('---\n')
                        md_file.write('\n')
                        

# Verwendung
create_md_files('../../data/species', '../../content/skolopender/taxonomie/scolopendra')