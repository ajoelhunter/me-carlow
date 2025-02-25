# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:57:15 2025

@author: Andrew Hunter
"""

import pandas as pd

# Load datasets
pokemon_species = pd.read_csv("../data/pokemon_species.csv")
generations = pd.read_csv("../data/generations.csv")

# Rename 'id' in generations to 'generation_id' for merging
generations = generations.rename(columns={"id": "generation_id"})

# Merge datasets on generation_id
merged_df = pokemon_species.merge(generations, on="generation_id", how="inner")

# Debugging: Print column names after merging
print("Merged DataFrame Columns:", merged_df.columns)

# Save the full merged dataset to q1.out
merged_df.to_csv("../q1.out", index=False)

# Extract required columns
result_df = merged_df[["identifier", "generation_id"]]
result_df.columns = ["Pokemon Name", "Generation ID"]

# Save to q1.csv
result_df.to_csv("../q1.csv", index=False)

print("Files q1.out and q1.csv have been successfully created in the HW5 folder.")
