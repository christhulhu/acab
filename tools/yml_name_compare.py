import yaml

def process_data(input_file):
    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    process_data = []

    for i in data:
        temp = {}
        temp['name'] = i['name']
        for a in i:
            if a != 'name':
                temp[a] = i[a]
        
        print(temp)

        process_data.append(temp)

    with open("../../data/scolopendra_species_valid_sorted.yml", 'w') as f:
        yaml.dump(process_data, f)

# Verwendung des Skripts
process_data('../../data/scolopendra_species_valid.yml')

