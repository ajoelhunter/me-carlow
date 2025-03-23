# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 22:27:43 2025

@author: Andrew Hunter
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load datasets
pokemon = pd.read_csv("../hw6_data/pokemon.csv")  # Contains height, weight, and base_experience

# prompts for 2 names
valid_pokemon = pokemon['identifier'].str.lower().unique()  
print("Valid Pokémon names:", valid_pokemon)

pokemon1 = input("Enter the first Pokémon name (e.g., Pikachu, Charizard): ").strip().lower()
pokemon2 = input("Enter the second Pokémon name (e.g., Pikachu, Charizard): ").strip().lower()

# validate input
if pokemon1 not in valid_pokemon or pokemon2 not in valid_pokemon:
    print(f"Error: One or both Pokémon names are invalid. Valid Pokémon names are: {', '.join(valid_pokemon)}")
else:
    # filter data
    pokemon1_data = pokemon[pokemon['identifier'].str.lower() == pokemon1]
    pokemon2_data = pokemon[pokemon['identifier'].str.lower() == pokemon2]

    # chec kif data bnot found
    if pokemon1_data.empty or pokemon2_data.empty:
        print(f"Error: Data for one or both Pokémon not found.")
    else:
        # extract height, weight, etc.
        height1, weight1, base_exp1 = pokemon1_data[['height', 'weight', 'base_experience']].values[0]
        height2, weight2, base_exp2 = pokemon2_data[['height', 'weight', 'base_experience']].values[0]

        # calculkate strength
        strength1 = (5 * height1) + (2 * weight1) + base_exp1
        strength2 = (5 * height2) + (2 * weight2) + base_exp2

        # create x shaped graph
        fig, axes = plt.subplots(3, 3, figsize=(15, 15))
        fig.suptitle(f"Comparison of {pokemon1.capitalize()} and {pokemon2.capitalize()}", fontsize=16)

        axes[0, 0].bar(['Height', 'Weight', 'Base Exp'], [height1, weight1, base_exp1], color=['blue', 'green', 'red'])
        axes[0, 0].set_title(f"{pokemon1.capitalize()} Attributes")
        axes[0, 0].set_ylabel("Value")

        axes[0, 2].bar(['Height', 'Weight', 'Base Exp'], [height2, weight2, base_exp2], color=['blue', 'green', 'red'])
        axes[0, 2].set_title(f"{pokemon2.capitalize()} Attributes")
        axes[0, 2].set_ylabel("Value")

        levels = np.arange(0, 101)
        experience1 = base_exp1 * levels  
        axes[2, 0].plot(levels, experience1, label='Experience', color='purple')
        axes[2, 0].set_title(f"{pokemon1.capitalize()} Experience Growth")
        axes[2, 0].set_xlabel("Level")
        axes[2, 0].set_ylabel("Experience")
        axes[2, 0].legend()


        experience2 = base_exp2 * levels  
        axes[2, 2].plot(levels, experience2, label='Experience', color='orange')
        axes[2, 2].set_title(f"{pokemon2.capitalize()} Experience Growth")
        axes[2, 2].set_xlabel("Level")
        axes[2, 2].set_ylabel("Experience")
        axes[2, 2].legend()

        # compare strength and shwo stronger mon
        if strength1 > strength2:
            stronger_pokemon = pokemon1.capitalize()
        elif strength2 > strength1:
            stronger_pokemon = pokemon2.capitalize()
        else:
            stronger_pokemon = "Both Pokémon are equally strong!"

        axes[1, 1].text(0.5, 0.5, stronger_pokemon, fontsize=20, ha='center', va='center')
        axes[1, 1].axis('off')  # Hide axes for the center graph

        # hide empty plots
        axes[0, 1].axis('off')
        axes[1, 0].axis('off')
        axes[1, 2].axis('off')
        axes[2, 1].axis('off')

        # show plot after adjustment
        plt.tight_layout()
        plt.show()