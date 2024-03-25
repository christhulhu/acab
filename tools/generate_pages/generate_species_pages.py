import os
import yaml

def create_md_files(src_folder, dest_folder):
    for dir in os.listdir(src_folder):
        for filename in os.listdir(os.path.join(src_folder, dir)):
            if filename.endswith('.yml'):
                with open(os.path.join(src_folder, dir, filename), 'r') as file:
                    data = yaml.safe_load(file)
                    if 'name' in data:
                        genus = data['taxonomy']['genus']
                        genus = genus.lower()
                        new_folder_name = filename.split('_')[-1].replace('.yml', '')
                        new_folder = os.path.join(dest_folder, genus, new_folder_name)
                        os.makedirs(new_folder, exist_ok=True)
                        with open(os.path.join(new_folder, 'index.md'), 'w') as md_file:
                            md_file.write('---\n')
                            md_file.write('title: ' + data['name'] + '\n')
                            md_file.write('description: Species ' + data['name'] + '\n')
                            md_file.write('bookHidden: true\n')
                            md_file.write('type: page\n')
                            md_file.write('layout: taxonomy_species\n')
                            md_file.write('datafile: ' + filename.replace('.yml', '') + '\n')
                            md_file.write('genus: ' + data['taxonomy']['genus']+'\n')
                            md_file.write('---\n')
                            md_file.write('\n')
                            md_file.write('{{<disclaimer/taxonomy-species>}}')
                        

# Verwendung
create_md_files('../../data/species/', '../../content/skolopender/taxonomie/scolopendromorpha/')