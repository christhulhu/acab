import os
import yaml

def find_keys_named_genera(d, result=None):
    if result is None:
        result = []

    if isinstance(d, dict):
        for key, value in d.items():
            if key == "genera":
                for v in value:
                    result.append(v)
            elif isinstance(value, (dict, list)):
                find_keys_named_genera(value, result)
    elif isinstance(d, list):
        for item in d:
            if isinstance(item, (dict, list)):
                find_keys_named_genera(item, result)

    return result

def create_md_files(src_file, dest_folder):
    with open(src_file, 'r') as file:
        data = yaml.safe_load(file)
        genera = find_keys_named_genera(data)
        for genus in genera:
            genus_lower = genus.lower()
            new_folder = os.path.join(dest_folder, genus_lower)
            os.makedirs(new_folder, exist_ok=True)
            with open(os.path.join(new_folder, '_index.md'), 'w') as md_file:
                md_file.write('---\n')
                md_file.write('title: ' + genus + '\n')
                md_file.write('description: Gattung ' + genus + '\n')
                md_file.write('bookHidden: true\n')
                md_file.write('type: page\n')
                md_file.write('layout: taxonomy_genus\n')
                md_file.write('datadir: ' + genus_lower + '\n')
                md_file.write('---\n')
                md_file.write('\n')
                md_file.write('# Die Gattung: ' + genus)
                md_file.write('\n')
                md_file.write('{{<disclaimer/taxonomy-genus>}}')

                        

# Verwendung
create_md_files('../../data/taxonomy.yml', '../../content/skolopender/taxonomie/scolopendromorpha/')