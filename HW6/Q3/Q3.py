# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 21:38:40 2025

@author: Andrew Hunter
"""

import pandas as pd
import matplotlib.pyplot as plt

#  loads datasets
pokemon_species = pd.read_csv("../hw6_data/pokemon_species.csv")  # Contains generation info
pokemon = pd.read_csv("../hw6_data/pokemon.csv")                  # Contains height, weight, and base_experience

# merge datasets
pokemon_data = pd.merge(pokemon, pokemon_species, left_on='species_id', right_on='id')

# calculate strength
pokemon_data['strength'] = (5 * pokemon_data['height']) + (2 * pokemon_data['weight']) + pokemon_data['base_experience']

# prompt for pokemon name
valid_pokemon = pokemon_data['identifier_x'].str.lower().unique()  # get valid names
print("Valid Pokémon names:", valid_pokemon)

user_pokemon = input("Enter a Pokemon name (e.g., Pikachu, Charizard): ").strip().lower()  # convert to lowercase

# validate input
if user_pokemon not in valid_pokemon:
    print(f"Error: '{user_pokemon}' is not a valid Pokémon name. Please check your input.")
else:
    # fitler data
    filtered_data = pokemon_data[pokemon_data['identifier_x'].str.lower() == user_pokemon]

    # check if data is found
    if filtered_data.empty:
        print(f"No data found for Pokémon '{user_pokemon}'.")
    else:
        # group by generation
        strength_per_generation = filtered_data.groupby('generation_id')['strength'].mean().reset_index()
        strength_per_generation.columns = ['Generation', 'Strength']

        # plot results
        plt.figure(figsize=(10, 6))
        plt.bar(strength_per_generation['Generation'], strength_per_generation['Strength'], color='skyblue')
        plt.xlabel('Generation', fontsize=12)
        plt.ylabel('Strength', fontsize=12)
        plt.title(f'Strength of {user_pokemon.capitalize()} Over Generations', fontsize=14)
        plt.xticks(strength_per_generation['Generation'])  # Ensure x-axis labels are integers
        plt.tight_layout()  # Adjust layout to prevent label overlap

        # annotatyions
        for index, row in strength_per_generation.iterrows():
            plt.text(row['Generation'], row['Strength'], f"{row['Strength']:.2f}", ha='center', va='bottom')

        # show plot
        plt.show()