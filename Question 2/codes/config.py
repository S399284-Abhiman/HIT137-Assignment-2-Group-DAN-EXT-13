# ==========================================================
# Configuration file for Temperature Analysis project.
# Contains folder paths, output filenames, month names, and season mapping.
# ==========================================================

# Folder containing CSV temperature data

DATA_FOLDER = "temperatures"

# Output files
OUTPUT_AVG_FILE = "average_temp.txt"
OUTPUT_RANGE_FILE = "largest_temp_range_station.txt"
OUTPUT_STABILITY_FILE = "temperature_stability_stations.txt"

# Month names
months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']

# Mapping of months to Australian seasons
month_to_season_map = {
    'January': 'Summer', 'February': 'Summer', 'March': 'Autumn',
    'April': 'Autumn', 'May': 'Autumn', 'June': 'Winter',
    'July': 'Winter', 'August': 'Winter', 'September': 'Spring',
    'October': 'Spring', 'November': 'Spring', 'December': 'Summer'
}
