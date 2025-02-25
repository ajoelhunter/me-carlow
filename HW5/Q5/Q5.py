# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:52:29 2025

@author: Andrew Hunter
"""

import pandas as pd
import matplotlib.pyplot as plt

# load datasets
pokemon = pd.read_csv("../data/pokemon.csv")
pokemon_types = pd.read_csv("../data/pokemon_types.csv")
pokemon_species = pd.read_csv("../data/pokemon_species.csv")

# create mapping
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

# map the type_id
pokemon_types['type_name'] = pokemon_types['type_id'].map(type_id_to_name)

# merge
pokemon_data = pd.merge(pokemon, pokemon_types, left_on='id', right_on='pokemon_id')
pokemon_data = pd.merge(pokemon_data, pokemon_species, left_on='species_id', right_on='id')

# add type color
def type_to_color(pokemon_type):
    type_colors = {
        'fire': 'red',
        'water': 'blue',
        'grass': 'green',
        'electric': 'yellow',
        'bug': 'brown',
        'normal': 'gray',
        'ghost': 'purple',
        'dragon': 'cyan',
        'psychic': 'pink',
        'rock': 'darkgray',
        'ice': 'lightblue',
        'fighting': 'orange',
        'fairy': 'violet',
        'poison': 'purple',
        'ground': 'saddlebrown',
        'steel': 'silver',
        'dark': 'black',
    }
    return type_colors.get(pokemon_type, 'gray')  # Default to 'gray' if the type is not found

# apply function
pokemon_data['type_color'] = pokemon_data['type_name'].apply(lambda x: type_to_color(x))
type_counts = pokemon_data.groupby('type_name')['type_color'].count().reset_index()

# write result
type_counts.to_csv("q5.out", index=False)

# plot results
plt.figure(figsize=(12, 6))

# plot bar
plt.bar(type_counts['type_name'], type_counts['type_color'], color=type_counts['type_color'])

# add labels
plt.xlabel('Pokemon Type', fontsize=12)
plt.ylabel('Count of Pokémon', fontsize=12)
plt.title('Number of Pokémon for Each Type', fontsize=14)

# rotate x-axis labels
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# show plot
plt.show()
