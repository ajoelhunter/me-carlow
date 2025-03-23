# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 22:20:37 2025

@author: Andrew Hunter
"""

import pandas as pd
import matplotlib.pyplot as plt

# loa up datasets
pokemon_types = pd.read_csv("../hw6_data/pokemon_types.csv")  
types = pd.read_csv("../hw6_data/types.csv")                  
pokemon_species = pd.read_csv("../hw6_data/pokemon_species.csv")  
pokemon = pd.read_csv("../hw6_data/pokemon.csv")             

# merge the datasets
pokemon_with_types = pd.merge(pokemon_types, types, left_on='type_id', right_on='id')

# merge for generation data
pokemon_with_generations = pd.merge(pokemon_with_types, pokemon_species, left_on='pokemon_id', right_on='id')

# merge for heigh, weight, etc.
pokemon_data = pd.merge(pokemon_with_generations, pokemon, left_on='pokemon_id', right_on='id')

# calculate strength
pokemon_data['strength'] = (5 * pokemon_data['height']) + (2 * pokemon_data['weight']) + pokemon_data['base_experience']

# prompt user for type
valid_types = types['identifier'].str.lower().unique()  
print("Valid Pokemon types:", valid_types)

user_type = input("Enter a Pokémon type (e.g., Electric, Fire, Water): ").strip().lower()  

# validate user input
if user_type not in valid_types:
    print(f"Error: '{user_type}' is not a valid Pokémon type. Valid types are: {', '.join(valid_types)}")
else:
    # filter data
    filtered_data = pokemon_data[pokemon_data['identifier_x'].str.lower() == user_type]

    # check for found data
    if filtered_data.empty:
        print(f"No Pokémon of type '{user_type}' found in the dataset.")
    else:
        # group by generations
        strength_stats = filtered_data.groupby('generation_id_y')['strength'].agg(['mean', 'min', 'max']).reset_index()
        strength_stats.columns = ['Generation', 'Average Strength', 'Minimum Strength', 'Maximum Strength']

        # plot results
        plt.figure(figsize=(12, 6))
        plt.plot(strength_stats['Generation'], strength_stats['Average Strength'], label='Average Strength', marker='o', color='blue')
        plt.plot(strength_stats['Generation'], strength_stats['Minimum Strength'], label='Minimum Strength', marker='o', color='red')
        plt.plot(strength_stats['Generation'], strength_stats['Maximum Strength'], label='Maximum Strength', marker='o', color='green')

        # labels
        plt.xlabel('Generation', fontsize=12)
        plt.ylabel('Strength', fontsize=12)
        plt.title(f'Strength Statistics for {user_type.capitalize()} Pokémon per Generation', fontsize=14)
        plt.xticks(strength_stats['Generation'])  # Ensure x-axis labels are integers
        plt.legend() 
        plt.grid(True)  
        plt.tight_layout()  

        # show plot
        plt.show()