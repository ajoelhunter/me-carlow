# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:42:21 2025

@author: darkm
"""


import pandas as pd
import matplotlib.pyplot as plt
import random

# Load the datasets
pokemon_species = pd.read_csv("../data/pokemon_species.csv")
pokemon_colors = pd.read_csv("../data/pokemon_colors.csv")
pokemon = pd.read_csv("../data/pokemon.csv")

# Check the column names of the pokemon dataset to verify base_experience
print(pokemon.columns)