# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:36:54 2025

@author: Andrew Hunter
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
regions = pd.read_csv("../data/regions.csv")
locations = pd.read_csv("../data/locations.csv")

# Count the number of Pokémon in each region
region_pokemon_count = locations['region_id'].value_counts()

# Map region ids to names using the "identifier" column from regions.csv
region_names = regions.set_index('id')['identifier'].to_dict()
region_pokemon_count = region_pokemon_count.rename(region_names)

# Sort the data for better visualization
region_pokemon_count = region_pokemon_count.sort_values(ascending=False)

# Plot the data
plt.figure(figsize=(10, 6))
region_pokemon_count.plot(kind='bar')

# Add labels and title
plt.xlabel('Region', fontsize=12)
plt.ylabel('Number of Pokémon', fontsize=12)
plt.title('Number of Pokémon in Each Region', fontsize=14)

# Show the plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()