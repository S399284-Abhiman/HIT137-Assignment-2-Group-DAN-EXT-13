# ==========================================================
# Contains all temperature analysis functions for the Temperature Analysis project:
# - seasonal_average
# - temperature_range
# - temperature_stability
# ==========================================================

import numpy as np
import pandas as pd
from config import months, month_to_season_map, OUTPUT_AVG_FILE, OUTPUT_RANGE_FILE, OUTPUT_STABILITY_FILE

def seasonal_average(df):

# Calculate seasonal average temperatures across all stations.


    season_data = {'Summer': [], 'Autumn': [], 'Winter': [], 'Spring': []}

    for season in season_data.keys():
        # Get months corresponding to this season
        season_months = [m for m in months if month_to_season_map[m] == season]
        # Flatten all station temperatures for these months and convert to numeric
        values = pd.to_numeric(df[season_months].values.flatten(), errors='coerce')
        # Remove NaN values
        season_data[season] = values[~pd.isna(values)]

    # Write seasonal averages to file with UTF-8 encoding
    with open(OUTPUT_AVG_FILE, "w", encoding="utf-8") as f:
        for season in ['Summer','Autumn','Winter','Spring']:
            avg_temp = np.mean(season_data[season])
            f.write(f"{season}: {avg_temp:.1f}°C\n")

    print(f"Seasonal averages saved to '{OUTPUT_AVG_FILE}'")


def temperature_range(df):

# Calculate temperature range (max - min) for each station and save the station(s) with the largest range.


    range_list = []

    for idx, row in df.iterrows():
        # Convert row to numeric, ignore invalid entries
        temps = pd.to_numeric(row[months], errors='coerce')
        temps = temps[~temps.isna()].values  # remove NaNs
        temp_range = temps.max() - temps.min()
        range_list.append((row['STATION_NAME'], temp_range, temps.max(), temps.min()))

    # Find maximum range and all stations with that range
    max_range = max(r[1] for r in range_list)
    largest_stations = [r for r in range_list if np.isclose(r[1], max_range)]

    # Write results to file with UTF-8 encoding
    with open(OUTPUT_RANGE_FILE, "w", encoding="utf-8") as f:
        for s in largest_stations:
            f.write(f"Station {s[0]}: Range {s[1]:.1f}°C (Max: {s[2]:.1f}°C, Min: {s[3]:.1f}°C)\n")

    print(f"Largest temperature range saved to '{OUTPUT_RANGE_FILE}'")


def temperature_stability(df):

# Calculate temperature stability (standard deviation) for each station.


    std_list = []

    for idx, row in df.iterrows():
        # Convert row to numeric, ignore invalid entries
        temps = pd.to_numeric(row[months], errors='coerce')
        temps = temps[~temps.isna()].values  # remove NaNs
        std = np.std(temps)
        std_list.append((row['STATION_NAME'], std))

    std_values = [s[1] for s in std_list]
    min_std = min(std_values)
    max_std = max(std_values)

    # Identify stations with minimum and maximum standard deviation
    most_stable = [s for s in std_list if np.isclose(s[1], min_std)]
    most_variable = [s for s in std_list if np.isclose(s[1], max_std)]

    # Write results to file with UTF-8 encoding
    with open(OUTPUT_STABILITY_FILE, "w", encoding="utf-8") as f:
        for s in most_stable:
            f.write(f"Most Stable: Station {s[0]}: StdDev {s[1]:.1f}°C\n")
        for s in most_variable:
            f.write(f"Most Variable: Station {s[0]}: StdDev {s[1]:.1f}°C\n")

    print(f"Temperature stability saved to '{OUTPUT_STABILITY_FILE}'")
