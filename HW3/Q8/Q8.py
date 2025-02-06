# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:06:10 2025

@author: Andrew Hunter
"""

import pandas as pd
import os

def load_pokemon_data():
    """Loads the Pokémon dataset and returns it as a DataFrame."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(current_dir, "..")  # Move up from q6 to hw3
    csv_path = os.path.join(root_path, "data", "poke.csv")
    
    # Read the CSV file
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("Error: File not found at path:", csv_path)
        return None
    except Exception as e:
        print("Error reading file:", e)
        return None
    
    return df

def get_pokemon_by_number():
    """Prompts the user for a number and returns the Pokémon at that index 
    and the Pokémon with that ID within a single DataFrame."""
    
    df = load_pokemon_data()
    if df is None:
        return
    
    # Ensure column names are in lowercase and strip spaces
    df.columns = df.columns.str.strip().str.lower()

    attempt = 0  # Counter for attempts
    while attempt < 2:
        user_input = input("Enter a number: ").strip()

        # Check if input is a valid number
        if not user_input.isdigit():
            if attempt == 0:
                print("Please provide a number.")
            else:
                print("Error")
                return  # Exit after second invalid input
            attempt += 1
            continue

        # Convert input to an integer
        num = int(user_input)

        # Get Pokémon by index (if within range)
        index_pokemon = df.iloc[num:num+1] if 0 <= num < len(df) else pd.DataFrame()

        # Get Pokémon by ID (if exists)
        id_pokemon = df[df['id'] == num]

        # Combine both results into a single DataFrame
        result = pd.concat([index_pokemon, id_pokemon]).drop_duplicates()

        if result.empty:
            print("No Pokémon found for this number.")
        else:
            print(result)

        return  # Exit after successful operation

if __name__ == "__main__":
    get_pokemon_by_number()