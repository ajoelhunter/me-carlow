# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 22:44:41 2025

@author: Andrew Hunter
"""

import pandas as pd
import matplotlib.pyplot as plt

# load up the datasets
pokemon_types = pd.read_csv("../hw6_data/pokemon_types.csv")
types = pd.read_csv("../hw6_data/types.csv")

# merge pokemon types with the types to get the type names
pokemon_types = pd.merge(pokemon_types, types, left_on='type_id', right_on='id')

# Count the number of pokemon for each type
type_counts = pokemon_types['identifier'].value_counts().reset_index()
type_counts.columns = ['Type', 'Count']

# sort the data for better to make it look better
type_counts = type_counts.sort_values('Count', ascending=False)

# plot the results
plt.figure(figsize=(12, 6))
plt.bar(type_counts['Type'], type_counts['Count'], color='skyblue')
plt.xlabel('Pokémon Type', fontsize=12)
plt.ylabel('Number of Pokémon', fontsize=12)
plt.title('Number of Pokémon per Type', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent label overlap

# show the plot
plt.show()