# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:06:10 2025

@author: Andrew Hunter
"""

import pandas as pd
import os

def load_data():
    """Loads the regions and locations datasets."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(current_dir, "..")  # Move up from q6 to hw3
    data_folder = os.path.join(root_path, "data")  
    
    # Define file paths
    regions_path = os.path.join(data_folder, "regions.csv")
    locations_path = os.path.join(data_folder, "locations-2.csv")

    # Load datasets
    try:
        regions_df = pd.read_csv(regions_path)
        locations_df = pd.read_csv(locations_path)
    except FileNotFoundError:
        print("Error: One or more files were not found in the data folder.")
        return None, None
    except Exception as e:
        print("Error reading files:", e)
        return None, None

    # Ensure column names are formatted correctly
    regions_df.columns = regions_df.columns.str.strip().str.lower()
    locations_df.columns = locations_df.columns.str.strip().str.lower()

    return regions_df, locations_df

def count_locations_in_region():
    """Accepts a region name from the user and returns the number of locations in that region."""
    regions_df, locations_df = load_data()
    
    if regions_df is None or locations_df is None:
        return
    
    # Ensure necessary columns exist
    if 'id' not in regions_df.columns or 'identifier' not in regions_df.columns:
        print("Error: 'regions.csv' is missing required columns.")
        return
    if 'region_id' not in locations_df.columns:
        print("Error: 'locations-2.csv' is missing required columns.")
        return
    
    # Prompt user for a region name
    region_name = input("Enter a region name: ").strip().lower()

    # Check if the region exists
    region_match = regions_df[regions_df['identifier'].str.lower() == region_name]
    
    if region_match.empty:
        print("This region does not exist.")
        return

    # Get the region ID
    region_id = region_match['id'].values[0]

    # Count locations in the region
    location_count = locations_df[locations_df['region_id'] == region_id].shape[0]

    print(f"The region '{region_name.capitalize()}' has {location_count} locations.")

# Run the function
if __name__ == "__main__":
    count_locations_in_region()