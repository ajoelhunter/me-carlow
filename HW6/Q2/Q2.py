# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 20:53:47 2025

@author: Andrew Hunter
"""

import pandas as pd
import matplotlib.pyplot as plt

# loads the datasets
pokemon_types = pd.read_csv("../hw6_data/pokemon_types.csv")
types = pd.read_csv("../hw6_data/types.csv")
pokemon_species = pd.read_csv("../hw6_data/pokemon_species.csv")

# megres pokemon to get the type
pokemon_types = pd.merge(pokemon_types, types, left_on='type_id', right_on='id')

pokemon_data = pd.merge(pokemon_types, pokemon_species, left_on='pokemon_id', right_on='id')

# valid typing for checking
valid_types = types['identifier'].str.lower().unique()


# prompts the user for the type
user_type = input("Enter a Pokémon type (e.g., Electric, Fire, Water): ").strip().lower()  # Convert to lowercase

# check if type is valid
if user_type not in valid_types:
    print(f"Error: '{user_type}' is not a valid Pokémon type. Valid types are: {', '.join(valid_types)}")
else:
    # filter data
    filtered_data = pokemon_data[pokemon_data['identifier_x'].str.lower() == user_type]

    # Print the filtered data for debugging
    print(f"Filtered data for type '{user_type}':")
    print(filtered_data[['identifier_x', 'generation_id_y']].head())

    # check for data
    if filtered_data.empty:
        print(f"No Pokémon of type '{user_type}' found in the dataset.")
    else:
        # count the pokemon per generation
        type_per_generation = filtered_data['generation_id_y'].value_counts().sort_index().reset_index()
        type_per_generation.columns = ['Generation', 'Count']

        # plot
        plt.figure(figsize=(10, 6))
        plt.bar(type_per_generation['Generation'], type_per_generation['Count'], color='skyblue')
        plt.xlabel('Generation', fontsize=12)
        plt.ylabel('Number of Pokémon', fontsize=12)
        plt.title(f'Number of {user_type.capitalize()} Pokémon per Generation', fontsize=14)
        plt.xticks(type_per_generation['Generation'])  # Ensure x-axis labels are integers
        plt.tight_layout()  # Adjust layout to prevent label overlap

        # annotate vbars
        for index, row in type_per_generation.iterrows():
            plt.text(row['Generation'], row['Count'], str(row['Count']), ha='center', va='bottom')

        # show plot
        plt.show()