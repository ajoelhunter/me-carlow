# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:31:23 2025

@author: Andrew Hunter
"""

import csv
import os

# function that gives user the ability to search pokemon
def search_pokemon(file_name, pokemon_name):
    # go to root folder to find data folder for pokemon.csv
    hw1_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
    
    file_path = os.path.join(hw1_dir, 'data', file_name)
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # check for id and name
            if row[1].strip().lower() == pokemon_name.lower():  # checks for case sensitivity
                return row[0], row[1]  # returns the ID and name
    return None

# ask user for pokemon, then check file for pokemon
pokemon_name = input("Please enter the name of the Pokémon: ").strip()

pokemon_result = search_pokemon('poke.csv', pokemon_name)

if pokemon_result:
    #if pokemon is found
    with open('q6.out', 'w') as out_file:
            out_file.write(f"ID: {pokemon_result[0]}, Name: {pokemon_result[1]}\n")
            print(f"Pokemon has been printed to file.")
else:
    # if the pokemon is not found, alert
    print("Pokemon not found")