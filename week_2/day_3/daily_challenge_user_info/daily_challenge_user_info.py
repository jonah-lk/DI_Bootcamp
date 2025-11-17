# Ask a user for the following inputs 5 times:
# Name (string)
# Age (int)
# Score (int)
# Build a list of tuples using these inputs, each tuple should contain a name, age and score.

import os
import re

entries = []

while len(entries) < 5:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print('Provide the following. If you input invalid data you\'ll start over!')

    name = input('A name: (alpha only)\t')
    if not re.match(r'^[A-Za-z]+$', name):
        continue

    try:
        age = int(input('An age: (integer)\t'))
        if not re.match(r'^\d+$', str(age)):
            continue
        
        score = int(input('A score: (integer)\t'))
        if not re.match(r'^\d+$', str(score)):
            continue

        entry = (name, age, score)
        entries.append(entry)
    except:
        continue

entries = sorted(entries, key = lambda entry: (entry[0], entry[1], entry[2]))

print(entries)