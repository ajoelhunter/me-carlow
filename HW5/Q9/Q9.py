# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 01:36:22 2025

@author: Andrew Hunter
"""

import pandas as pd
import numpy as np
import random

# load datasets
pokemon = pd.read_csv("../data/pokemon.csv")
pokemon_species = pd.read_csv("../data/pokemon_species.csv")

# merge pokemon data
pokemon_data = pd.merge(pokemon, pokemon_species, left_on='species_id', right_on='id')

pokemon_data = pokemon_data[['identifier_x', 'base_experience']]

# rename to identifier
pokemon_data.rename(columns={'identifier_x': 'identifier'}, inplace=True)

# generate a 4x4 dungeon
dungeon_size = 4
dungeon = np.empty((dungeon_size, dungeon_size), dtype=object)

# choose start and finish randomly
start_pos = (0, 0)
exit_pos = (random.randint(0, 3), random.randint(0, 3))
while exit_pos == start_pos:
    exit_pos = (random.randint(0, 3), random.randint(0, 3))

# fill up the dungeon with random pokemon
for i in range(dungeon_size):
    for j in range(dungeon_size):
        if (i, j) != start_pos and (i, j) != exit_pos:
            dungeon[i, j] = random.choice(pokemon_data[['identifier', 'base_experience']].values.tolist())

# team builder
team = []
print("Build your team of up to 6 Pokémon (type 'random' to generate a team)")
while len(team) < 6:
    choice = input("Enter Pokémon name or 'random': ")
    if choice.lower() == "random":
        team = random.sample(pokemon_data[['identifier', 'base_experience']].values.tolist(), 6)
        break
    elif choice in pokemon_data['identifier'].values:
        team.append(pokemon_data[pokemon_data['identifier'] == choice][['identifier', 'base_experience']].values[0].tolist())
    else:
        print("Invalid Pokémon. Try again.")
    if len(team) >= 6:
        break
print("Your team:", team)

# dungeon display
def display_dungeon():
    for i in range(dungeon_size):
        row = ""
        for j in range(dungeon_size):
            if (i, j) == tuple(player_pos):
                row += "[P] "
            elif (i, j) == exit_pos:
                row += "[ ] "
            else:
                row += "[ ] "
        print(row)
    print()

# navigation
player_pos = list(start_pos)
while player_pos != list(exit_pos) and len(team) > 0:
    display_dungeon()
    move = input("Move (WASD): ").lower()
    if move == 'w' and player_pos[0] > 0:
        player_pos[0] -= 1
    elif move == 's' and player_pos[0] < dungeon_size - 1:
        player_pos[0] += 1
    elif move == 'a' and player_pos[1] > 0:
        player_pos[1] -= 1
    elif move == 'd' and player_pos[1] < dungeon_size - 1:
        player_pos[1] += 1
    else:
        print("Invalid move.")
        continue
    
    # battle encounter
    if tuple(player_pos) != exit_pos and dungeon[player_pos[0], player_pos[1]] is not None:
        wild_pokemon = dungeon[player_pos[0], player_pos[1]]
        print(f"Encountered {wild_pokemon[0]} (Base EXP: {wild_pokemon[1]})")
        if team[0][1] >= wild_pokemon[1]:
            print(f"{team[0][0]} defeated {wild_pokemon[0]}!")
        else:
            print(f"{team[0][0]} lost to {wild_pokemon[0]} and was removed from the team.")
            team.pop(0)
        dungeon[player_pos[0], player_pos[1]] = None
    
    if len(team) == 0:
        with open("status.out", "w") as f:
            f.write("Failure - Team depleted.")
        print("Game Over. Your team was defeated.")
        exit()

# succes
with open("status.out", "w") as f:
    f.write(f"Success - {len(team)} Pokémon remaining.")
print("You reached the exit! Congratulations!")
