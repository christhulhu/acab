import os
import yaml

result = []

def gather(steps, previous, current):
    result = []
    #print("From Current Step " + str(current) + " to Previous Step " + str(previous['step']))
    for branch in previous['branches']:
        if 'next' in branch:
            if branch['next'] == current:
                #print('adding result')
                result.append(branch['branch'])
                #if 'intermediate_result' in branch:
                #        result.append('**INTERMEDIATE RESULT**: ' + branch['intermediate_result'])
                if 'previous' in previous:
                    #print('Recursion from ' + str(previous['step']) + ' to ' + str(previous['previous']))
                    prev = get_step(steps, previous['previous'])
                    #print('    Recursive from from ' + str(previous))
                    #print('        going to ' + str(prev))
                    tmp = gather(steps, prev, previous['step'])
                    for t in tmp:
                        result.append(t)
    return result

def get_step(steps, step):
    for entry in steps:
        if entry['step'] == step:
            return entry
    return None

with open(os.path.join('../data/keys', '2020-scolopendromorpha-genera.yml'), 'r') as file:
    data = yaml.safe_load(file)
    steps = data['key']

    #print(steps)
    
    for step in steps:
        for branch in step['branches']:
            if 'result' in branch:
                current_result = {}
                current_result['name'] = branch['result']
                #print(branch['result'])
                current_result['diagnosis'] = []
                if 'branch' in branch:
                    current_result['diagnosis'].append(branch['branch'])
                    #print(branch['branch'])
                    #if 'intermediate_result' in branch:
                    #    current_result['diagnosis'].append('**INTERMEDIATE RESULT**: ' + branch['intermediate_result'])
                    if 'previous' in step:
                        res = gather(steps, get_step(steps, step['previous']), step['step'])
                        for r in res:
                            current_result['diagnosis'].append(r)
                result.append(current_result)

    for r in result:
        print(r['name'])
        for d in r['diagnosis']:
            print('    ' + d)
        print()
                    
