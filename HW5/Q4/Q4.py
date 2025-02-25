# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:41:21 2025

@author: Andrew Hunter
"""

import pandas as pd
import matplotlib.pyplot as plt
import random

# load datasets
pokemon_species = pd.read_csv("../data/pokemon_species.csv")
pokemon_colors = pd.read_csv("../data/pokemon_colors.csv")
pokemon = pd.read_csv("../data/pokemon.csv")

# merge
pokemon_data = pd.merge(pokemon, pokemon_species, left_on='species_id', right_on='id')
pokemon_data = pd.merge(pokemon_data, pokemon_colors, left_on='species_id', right_on='id')

# create new dataset
pokemon_experience_color = pokemon_data[['identifier_x', 'base_experience', 'identifier_y']]

# rename collumns
pokemon_experience_color.columns = ['name', 'base_experience', 'primary_color']

# write dataset
pokemon_experience_color.to_csv("q4.out", index=False)

#random select
random_pokemon = pokemon_experience_color.sample(n=10)

# plot graph
plt.figure(figsize=(12, 6))

# plot bars
for i, row in random_pokemon.iterrows():
    plt.bar(row['name'], row['base_experience'], color=row['primary_color'])

# add labels
plt.xlabel('Pokemon', fontsize=12)
plt.ylabel('Base Experience', fontsize=12)
plt.title('Base Experience of Randomly Selected Pokémon', fontsize=14)

# rotate x-axis labels
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# show the plot
plt.show()
