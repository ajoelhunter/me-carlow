# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:11:42 2025

@author: Andrew Hunter
"""

import pandas as pd
import random
import matplotlib.pyplot as plt

# load the data
pokemon_species = pd.read_csv("../data/pokemon_species.csv")

print(pokemon_species.columns)
