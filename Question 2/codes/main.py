# ==========================================================
# Main entry point for Temperature Analysis program.
# Loads data and runs all analysis functions.
# ==========================================================


from data_utils import load_all_csv
from config import DATA_FOLDER
from analysis import seasonal_average, temperature_range, temperature_stability

def main():
    
#Main function to control program execution.
    
# Load all CSV data
    temperature_data = load_all_csv(DATA_FOLDER)
    print("Columns loaded:", list(temperature_data.columns))  # Debug: verify column names

# Run analyses
    seasonal_average(temperature_data)
    temperature_range(temperature_data)
    temperature_stability(temperature_data)

if __name__ == "__main__":
    main()
