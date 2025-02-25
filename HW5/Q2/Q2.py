# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:09:54 2025

@author: Andrew Hunter
"""

import pandas as pd
import random
import matplotlib.pyplot as plt

# load in the datasets
pokemon_species = pd.read_csv("../data/pokemon_species.csv")

stat_column = "order"

# extract the collumns
pokemon_data = pokemon_species[["identifier", stat_column]].dropna()

#innitialize an empty team
team = []

# add pokemon
def add_pokemon(name):
    if len(team) >= 6:
        print("Your team is already full (6 Pokemon max).")
        return
    if name not in pokemon_data["identifier"].values:
        print("Pokemon not found in dataset.")
        return
    team.append(name)
    print(f"{name} added to your team!")

# generate a random team
def generate_random_team():
    global team
    team = random.sample(list(pokemon_data["identifier"].values), 6)
    print("Random team generated:", ", ".join(team))

# delete a Pokemon from the team
def delete_pokemon(name):
    if name in team:
        team.remove(name)
        print(f"{name} removed from your team.")
    else:
        print("Pokemon not in team.")

# display graph before exiting
def show_team_graph():
    if not team:
        print("No Pokemon in team to display graph.")
        return
    
    team_data = pokemon_data[pokemon_data["identifier"].isin(team)]
    plt.bar(team_data["identifier"], team_data[stat_column], color='skyblue')
    plt.xlabel("Pokemon")
    plt.ylabel(stat_column.replace("_", " ").title())
    plt.title(f"{stat_column.replace('_', ' ').title()} of Team Members")
    plt.xticks(rotation=45)
    plt.show()

# loop
while True:
    print("\nPokemon Team Builder")
    print("1. Add Pokemon")
    print("2. Generate Random Team")
    print("3. Delete Pokemon")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Enter Pokemon name: ").strip().lower()
        add_pokemon(name)
    elif choice == "2":
        generate_random_team()
    elif choice == "3":
        name = input("Enter Pokemon name to remove: ").strip().lower()
        delete_pokemon(name)
    elif choice == "4":
        show_team_graph()
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
