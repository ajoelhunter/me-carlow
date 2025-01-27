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
                # check for matching Pokemon name (case insensitive)
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
    
    while True:  # menu 
        print("\nMenu:")
        print("1) Add Pokemon")
        print("2) List Team")
        print("3) Drop Member")
        print("4) Exit")
        choice = input("").strip() 
        
        if choice == '1':
            # add Pokemon to team
            if len(team) >= 6:
                print("Max team size, please remove a pokemon to add more.")
                continue  # skip if team is full
                
            pokemon_name = input("Enter the name of the Pokemon (or type 'exit' to finish): ").strip()

            if pokemon_name.lower() == "exit":
                break  # exit if the user types 'exit'
            
            # search for the pokemon in poke.csv
            pokemon_result = search_pokemon('poke.csv', pokemon_name)

            if pokemon_result:
                # add pokemon to team
                team.append(pokemon_result)
                print(f"{pokemon_result[1]} added to your team!")
            else:
                # report error if pokemon not found
                print("Pokemon not found.")
        
        elif choice == '2':
            # List all team members
            if team:
                print("\nCurrent Team:")
                for idx, member in enumerate(team, start=1):
                    print(f"{idx}) {member[1]}")
            else:
                print("Your team is empty.")
        
        elif choice == '3':
            # remove a party member
            if team:
                print("\nCurrent Team:")
                for idx, member in enumerate(team, start=1):
                    print(f"{idx}) {member[1]}")
                
                try:
                    member_id = int(input("\nEnter the ID of the member to drop (or type '0' to cancel): "))
                    if member_id == 0:
                        print("Cancelled drop operation.")
                    elif 1 <= member_id <= len(team):
                        removed_member = team.pop(member_id - 1)  # Remove the member
                        print(f"{removed_member[1]} has been removed from your team.")
                    else:
                        print("Invalid ID, please try again.")
                except ValueError:
                    print("Invalid input.")
            else:
                print("Your team is empty.")
        
        elif choice == '4':
            # Exit and output the team
            try:
                with open('q9.out', 'w') as out_file:
                    if team:
                        out_file.write("Your Pokemon Team and Locations:\n")
                        for member in team:
                            pokemon_id = member[0]
                            pokemon_name = member[1]
                            # get the locations for this Pokemon ID from the location_dict
                            locations = location_dict.get(pokemon_id, [])
                            out_file.write(f"ID: {pokemon_id}, Name: {pokemon_name}, Locations: {', '.join(locations)}\n")
                    else:
                        out_file.write("No Pokemon were added to the team.\n")
                        
                        print("Your team and locations have been saved to q8.out.")
            except Exception as e:
                print(f"Error writing to file: {e}")
            break  # Exit the loop and the program

        else:
            print("error")

    
build_team()