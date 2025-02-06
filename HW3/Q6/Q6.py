# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:38:20 2025

@author: Andrew Hunter
"""

import pandas as pd
import os

def summarize_pokemon_data():
    # defines the path for the csv files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(current_dir, "..") 
    csv_path = os.path.join(root_path, "data", "poke.csv")
    
    #  read the file
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("Error: File not found at path:", csv_path)
        return
    except Exception as e:
        print("Error reading file:", e)
        return
    
    # get dataset summary
    num_rows, num_columns = df.shape
    column_names = df.columns.tolist()
    
    print(f"The pokemon dataset consists of {num_columns} columns and {num_rows} rows.")
    print("It has the following column names:", column_names)

if __name__ == "__main__":
    summarize_pokemon_data()