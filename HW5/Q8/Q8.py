# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 01:19:23 2025

@author: Andrew Hunter
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
pokemon_species = pd.read_csv("../data/pokemon_species.csv")
pokemon = pd.read_csv("../data/pokemon.csv")

# Filter for Mythical and Legendary Pokémon
legendary_mythical_pokemon = pokemon_species[(pokemon_species['is_legendary'] == 1) | (pokemon_species['is_mythical'] == 1)]

# Merge the datasets to include the base_experience, height, and weight
pokemon_data = pd.merge(legendary_mythical_pokemon, pokemon, left_on='id', right_on='species_id')

# Check the columns to verify we have 'identifier' from the pokemon dataset
print(pokemon_data.columns)

# Calculate the 'Strength' column
pokemon_data['Strength'] = (pokemon_data['base_experience'] * 5) + ((pokemon_data['height'] + pokemon_data['weight']) * 5)

# Sort the Pokémon by 'Strength' and select the top 5 strongest
strongest_pokemon = pokemon_data.sort_values('Strength', ascending=False).head(5)

# Write the result to q8.out
strongest_pokemon.to_csv("q8.out", index=False)

# Print the dataframe for verification
print(strongest_pokemon)

# Plot the results
plt.figure(figsize=(10, 6))

# Plot a bar chart comparing the 'Strength' values
# Use 'pokemon_data' columns to ensure we're accessing the correct names
plt.bar(strongest_pokemon['identifier'], strongest_pokemon['Strength'], color='teal')

# Add labels and title
plt.xlabel('Pokemon Name', fontsize=12)
plt.ylabel('Strength', fontsize=12)
plt.title('Top 5 Strongest Mythical and Legendary Pokémon', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Tight layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
