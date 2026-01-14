# ==========================================================
# Data utilities for Temperature Analysis project.
# Handles loading and combining all CSV files from the data folder.
# ==========================================================

import os
import pandas as pd

# Load all CSV files from the specified folder and combine them into a single DataFrame.

def load_all_csv(folder): 
    
    all_files = [f for f in os.listdir(folder) if f.endswith(".csv")]
    if not all_files:
        raise FileNotFoundError(f"No CSV files found in folder '{folder}'")


    df_list = []
    for f in all_files:
        path = os.path.join(folder, f)
        # Read CSV, handle BOM and remove extra spaces
        df = pd.read_csv(path, sep=',', encoding='utf-8-sig')
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.replace('\ufeff','')
        df_list.append(df)

    combined = pd.concat(df_list, ignore_index=True)
    return combined
