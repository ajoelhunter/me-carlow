# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:06:10 2025

@author: Andrew Hunter
"""
import pandas as pd
import os

def summarize_pokemon_data():
    # defines the path for the csv files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(current_dir, "..")  # Move up from q6 to hw3
    csv_path = os.path.join(root_path, "data", "poke.csv")
    
    # reads the file
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("Error: File not found at path:", csv_path)
        return None
    except Exception as e:
        print("Error reading file:", e)
        return None
    
    return df

def get_pokemon_data():
    # get dataframe
    df = summarize_pokemon_data()
    if df is None:
        return

    # convert column names to lowercase and strip spaces (just in case)
    df.columns = df.columns.str.strip().str.lower()

    # prompt user for the Pokémon name
    pokemon_name = input("Enter the name of a Pokémon: ").strip().lower()

    # check if the pokemon exists in the dataset
    if pokemon_name in df['identifier'].str.lower().values:
        # filter dataframe for pokemon
        pokemon_data = df[df['identifier'].str.lower() == pokemon_name]
        print(pokemon_data)
    else:
        print("This Pokémon does not exist.")

if __name__ == "__main__":
    get_pokemon_data()