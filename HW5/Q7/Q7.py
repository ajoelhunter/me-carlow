# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 01:05:12 2025

@author: Andrew Hunter
"""

import pandas as pd

# load datasets
pokemon_species = pd.read_csv("../data/pokemon_species.csv")

# filter
legendary_mythical_pokemon = pokemon_species[(pokemon_species['is_legendary'] == 1) | (pokemon_species['is_mythical'] == 1)]

# write results
legendary_mythical_pokemon.to_csv("q7.out", index=False)

# print first dew rows
print(legendary_mythical_pokemon.head())
