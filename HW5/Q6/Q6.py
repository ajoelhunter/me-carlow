# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:57:15 2025

@author: Andrew Hunter
"""

import pandas as pd

# load datasets
pokemon_types = pd.read_csv("../data/pokemon_types.csv")
type_id_to_name = {
    1: 'fire',
    2: 'water',
    3: 'grass',
    4: 'electric',
    5: 'bug',
    6: 'normal',
    7: 'ghost',
    8: 'dragon',
    9: 'psychic',
    10: 'rock',
    11: 'ice',
    12: 'fighting',
    13: 'fairy',
    14: 'poison',
    15: 'ground',
    16: 'steel',
    17: 'dark',
}

# map type_id
pokemon_types['type_name'] = pokemon_types['type_id'].map(type_id_to_name)

# filter the secondary type
secondary_types = pokemon_types[pokemon_types['slot'] == 2]

# count the occurrences of each secondary type
secondary_type_counts = secondary_types['type_name'].value_counts().reset_index()

# rename columns
secondary_type_counts.columns = ['type_name', 'count']

# get most common secondary trype
most_common_secondary_type = secondary_type_counts.iloc[0]

# write the result to q6.out
with open("q6.out", "w") as f:
    f.write(f"Most Common Secondary Type: {most_common_secondary_type['type_name']}\n")
    f.write(f"Count: {most_common_secondary_type['count']}\n")

# Print the result to the console for verification
print(f"Most Common Secondary Type: {most_common_secondary_type['type_name']}")
print(f"Count: {most_common_secondary_type['count']}")
