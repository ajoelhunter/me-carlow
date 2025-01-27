# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:31:23 2025

@author: Andrew Hunter
"""

import csv
import os

# search for pokemon in database
def search_pokemon(file_name, pokemon_name):
    try:
        # go to root folder to find the data folder for poke.csv
        hw1_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
        file_path = os.path.join(hw1_dir, 'data', file_name)

        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                # check for matching Pokémon name (case insensitive)
                if row[1].strip().lower() == pokemon_name.lower():
                    return row[0], row[1]  # return ID and name
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

# location finder
def get_pokemon_locations():
    location_dict = {}
    try:
        # go to root folder for locations.csv
        hw1_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
        location_file_path = os.path.join(hw1_dir, 'data', 'locations.csv')
        
        with open(location_file_path, mode='r') as loc_file:
            csv_reader = csv.reader(loc_file)
            for row in csv_reader:
                pokemon_id = row[4]
                location = row[2]
                if pokemon_id not in location_dict:
                    location_dict[pokemon_id] = []
                location_dict[pokemon_id].append(location)
    except Exception as e:
        print(f"An error occurred while reading locations: {e}")
    return location_dict

#team builder
def build_team():
    team = []  # team list
    location_dict = get_pokemon_locations() #load location data 

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

    # output the team members to q8.out
    with open('q8.out', 'w') as out_file:
            if team:
                out_file.write("Your Pokemon Team and Locations:\n")
                for member in team:
                    pokemon_id = member[0]
                    pokemon_name = member[1]
                    locations = location_dict.get(pokemon_id, [])
                    out_file.write(f"ID: {pokemon_id}, Name: {pokemon_name}, Locations: {', '.join(locations)}\n")
            else:
                out_file.write("No Pokemon were added to the team.\n")

    print("Your team has been saved to q8.out.")

build_team()