import pandas as pd
import glob
import os

def analyze_temperatures(folder_path="temperatures"):
    # Create output folder if it doesn't exist
    if not os.path.exists("output"):
        os.makedirs("output")

    # Get all CSV files
    file_paths = glob.glob(os.path.join(folder_path, "*.csv"))

    if not file_paths:
        print("No CSV files found.")
        return

    # Combine all CSV data
    all_data = pd.DataFrame()

    for file in file_paths:
        df = pd.read_csv(file)

        # Ensure required columns exist
        required_cols = {'Station', 'Date', 'Temperature'}
        if not required_cols.issubset(df.columns):
            print(f"Skipping {file}: missing required columns")
            continue

        all_data = pd.concat([all_data, df], ignore_index=True)

    # Clean data
    all_data['Temperature'] = pd.to_numeric(all_data['Temperature'], errors='coerce')
    all_data = all_data.dropna(subset=['Temperature'])
    all_data['Date'] = pd.to_datetime(all_data['Date'])

    # Run analyses
    calculate_seasonal_average(all_data)
    find_largest_temp_range(all_data)
    analyze_temperature_stability(all_data)

    print("Analysis complete. Results saved in the output folder.")


# ----------- Seasonal Average -----------
def calculate_seasonal_average(df):
    def get_season(month):
        if month in [12, 1, 2]:
            return 'Summer'
        elif month in [3, 4, 5]:
            return 'Autumn'
        elif month in [6, 7, 8]:
            return 'Winter'
        else:
            return 'Spring'

    df['Season'] = df['Date'].dt.month.apply(get_season)
    seasonal_avg = df.groupby('Season')['Temperature'].mean()

    ordered_seasons = ['Summer', 'Autumn', 'Winter', 'Spring']

    with open("output/average_temp.txt", "w") as f:
        for season in ordered_seasons:
            if season in seasonal_avg:
                f.write(f"{season}: {seasonal_avg[season]:.1f}°C\n")


# ----------- Temperature Range -----------
def find_largest_temp_range(df):
    stats = df.groupby('Station')['Temperature'].agg(['max', 'min'])
    stats['Range'] = stats['max'] - stats['min']

    max_range = stats['Range'].max()
    largest = stats[stats['Range'] == max_range]

    with open("output/largest_temp_range_station.txt", "w") as f:
        for station, row in largest.iterrows():
            f.write(
                f"Station {station}: Range {row['Range']:.1f}°C "
                f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
            )


# ----------- Temperature Stability -----------
def analyze_temperature_stability(df):
    std_dev = df.groupby('Station')['Temperature'].std().dropna()

    min_std = std_dev.min()
    max_std = std_dev.max()

    most_stable = std_dev[std_dev == min_std]
    most_variable = std_dev[std_dev == max_std]

    with open("output/temperature_stability_stations.txt", "w") as f:
        f.write("Most Stable:\n")
        for station, val in most_stable.items():
            f.write(f"Station {station}: StdDev {val:.1f}°C\n")

        f.write("\nMost Variable:\n")
        for station, val in most_variable.items():
            f.write(f"Station {station}: StdDev {val:.1f}°C\n")


# ----------- Run Program -----------
if __name__ == "__main__":
    analyze_temperatures("temperatures")
