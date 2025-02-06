# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:58:05 2025

@author: Andrew Hunter
"""

import pandas as pd
import os

# loads up the datasets
def load_data():
    """Loads the pokemon, regions, and locations datasets."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(current_dir, "..")  
    data_folder = os.path.join(root_path, "data")  
    
    # defines the file paths
    pokemon_path = os.path.join(data_folder, "poke.csv")
    regions_path = os.path.join(data_folder, "regions.csv")
    locations_path = os.path.join(data_folder, "locations-2.csv")

    try:
        pokemon_df = pd.read_csv(pokemon_path)
        regions_df = pd.read_csv(regions_path)
        locations_df = pd.read_csv(locations_path)
    except FileNotFoundError:
        print("Error: One or more files were not found in the data folder.")
        return None, None, None
    except Exception as e:
        print("Error reading files:", e)
        return None, None, None

    # cleans up the data columns
    pokemon_df.columns = pokemon_df.columns.str.strip().str.lower()
    regions_df.columns = regions_df.columns.str.strip().str.lower()
    locations_df.columns = locations_df.columns.str.strip().str.lower()

    return pokemon_df, regions_df, locations_df

# search by the pokemons name
def search_by_name(pokemon_df):
    """Search for a Pokémon by name."""
    pokemon_name = input("Enter the name of the Pokémon: ").strip().lower()

    # checks if the pokemon exists
    if pokemon_name in pokemon_df['identifier'].str.lower().values:
        pokemon_data = pokemon_df[pokemon_df['identifier'].str.lower() == pokemon_name]
        # returns the data
        return pokemon_data[['identifier', 'id', 'height', 'weight']]
    else:
        print("This mysterious Pokémon cannot be found.")
        return None

# search by the region
def search_by_region(regions_df, locations_df):
    """Search for locations based on the region name."""
    region_name = input("Enter the name of the region: ").strip().lower()

    # checks if the region exists
    if region_name in regions_df['identifier'].str.lower().values:
        # finds the region ID
        region_id = regions_df[regions_df['identifier'].str.lower() == region_name]['id'].values[0]
        
        # grabs the locations for that region
        location_data = locations_df[locations_df['region_id'] == region_id]
        
        # returns the locations names
        return location_data[['identifier']]
    else:
        print("This region does not exist.")
        return None

# mian menu
def ash_pokemon_app():
    """Run Ash's Pokemon and Locations App."""
    # loads the data
    pokemon_df, regions_df, locations_df = load_data()
    
    if pokemon_df is None or regions_df is None or locations_df is None:
        return

    # loop
    while True:
        print("\nHello, Ash!")
        print("1) Search By Name")
        print("2) Search By Region")
        print("3) Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # search by pokemon name
            result = search_by_name(pokemon_df)
            if result is not None:
                print(result)
        elif choice == "2":
            # search by region
            result = search_by_region(regions_df, locations_df)
            if result is not None:
                print(result)
        elif choice == "3":
            print("Goodbye, Ash!")
            break  # exits the program
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    ash_pokemon_app()