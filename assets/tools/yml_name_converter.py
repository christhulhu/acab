import yaml

def process_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    processed_data = []
    synonyms = []

    for item in data:
        if item['status'] == 'valid':
            item['synonyms'] = []
            processed_data.append(item)
        elif item['status'] == 'Synonym':
            synonyms.append(item)
        else:
            item['synonyms'] = []
            processed_data.append(item)

    for synonym in synonyms:
        for item in processed_data:
            if item['name'] == synonym['current_name']:
                item['synonyms'].append({
                    'name': synonym['name'],
                    'first_description': synonym['first_description']
                })

    with open(output_file, 'w') as f:
        yaml.dump(processed_data, f)

# Verwendung des Skripts
process_data('scolopendra_species.yml', 'output.yml')

