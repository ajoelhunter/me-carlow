# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:31:23 2025

@author: Andrew Hunter
"""

import csv
import os

# search for pokemon in database
def search_pokemon(file_name, pokemon_name):
    # go to root folder to find the data folder for poke.csv
    hw1_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
    file_path = os.path.join(hw1_dir, 'data', file_name)
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Check for matching Pokémon name (case insensitive)
            if row[1].strip().lower() == pokemon_name.lower():
                return row[0], row[1]  # Return ID and name
    return None

#team builder
def build_team():
    team = []  # team list

    while len(team) < 6:  # keep team to 6
        pokemon_name = input("Enter the name of the Pokémon (or type 'exit' to finish): ").strip()

        if pokemon_name.lower() == "exit":
            break  
        
        # search for the Pokémon in poke.csv
        pokemon_result = search_pokemon('poke.csv', pokemon_name)

        if pokemon_result:
            # add to team if found
            team.append(pokemon_result)
            print(f"{pokemon_result[1]} added to your team!")
        else:
            # rport error if not found
            print("Pokemon not found, try again.")

    # output the team members to q7.out
    with open('q7.out', 'w') as out_file:
        if team:
            out_file.write("Your Pokemon Team:\n")
            for member in team:
                out_file.write(f"ID: {member[0]}, Name: {member[1]}\n")
        else:
            out_file.write("No Pokemon were added to the team.\n")

    print("Your team has been saved to q7.out.")

build_team()