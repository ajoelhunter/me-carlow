import pandas as pd
import os

def check_regions_columns():
    """Loads regions.csv and prints its column names."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(current_dir, "..")  
    regions_path = os.path.join(root_path, "data", "regions.csv")

    try:
        df = pd.read_csv(regions_path)
        print("Columns in regions.csv:", df.columns.tolist())  
    except FileNotFoundError:
        print("Error: 'regions.csv' not found.")
    except Exception as e:
        print("Error reading file:", e)

check_regions_columns()