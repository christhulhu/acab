import os
import yaml

def create_md_files(src_folder, dest_folder):
    for dir in os.listdir(src_folder):
        for filename in os.listdir(os.path.join(src_folder, dir)):
            if filename.endswith('.yml'):
                with open(os.path.join(src_folder, dir, filename), 'r') as file:
                    data = yaml.safe_load(file)
                    if 'publications' in data:
                        genus = data['taxonomy']['genus']
                        genus = genus.lower()
                        species_folder_name = filename.split('_')[-1].replace('.yml', '')
                        species_folder = os.path.join(dest_folder, genus, species_folder_name)
                        os.makedirs(species_folder, exist_ok=True)
                        data_folder = os.path.join(dest_folder, genus, species_folder_name, 'data')
                        os.makedirs(data_folder, exist_ok=True)

                        ref = []
                        for pub in data['publications']:
                            current_pub = {}
                            current_pub['year'] = pub['year']
                            current_pub['author'] = pub['author']
                            current_pub['title'] = pub['title']
                            if 'download' in pub:
                                current_pub['link'] = pub['download']
                            tmp = pub['author'].split(' ')[0].replace(',', '').lower()
                            print(tmp)
                            current_pub['id'] = str(pub['year']) + "-" + tmp
                            ref.append(current_pub)
                        

                        with open(os.path.join(data_folder, 'reference.yml'), 'w') as ref_file:
                            yaml.dump(ref, ref_file)
                        

# Verwendung
create_md_files('../../data/species/', '../../content/skolopender/taxonomie/scolopendromorpha/')