# QUESTION 2 – TEMPERATURE ANALYSIS PROGRAM

## OVERVIEW
This program analyzes temperature data from multiple weather stations in Australia.  
It calculates **seasonal averages**, identifies stations with the **largest temperature range**, and evaluates **temperature stability** across all stations.

The main focus of this solution is modular program design, clear data handling, and producing accurate output files.

---

## PROGRAM STRUCTURE
The solution is divided into multiple Python files to improve clarity and maintainability.

### Files included
- `codes/`
  - `main.py`
  - `config.py`
  - `data_utils.py`
  - `analysis.py`
- `temperatures/` (folder containing CSV files)
- `README.md`

---

## FILE DESCRIPTIONS

### config.py
Contains all configuration constants including:  
- Folder paths for input CSV files  
- Output filenames for generated results  
- Month names and their mapping to Australian seasons  

### data_utils.py
Handles loading and combining all CSV files from the `temperatures/` folder into a single pandas DataFrame.  
- Ensures BOM and whitespace in column names are handled correctly.  
- Raises an error if no CSV files are found.

### analysis.py
Calculates **seasonal averages** across all stations.  
- Flattens monthly data for each season.  
- Ignores missing values (`NaN`).  
- Writes results to `average_temp.txt`.

Calculates **temperature range** (Max - Min) for each station.  
- Identifies station(s) with the largest temperature range.  
- Writes results to `largest_temp_range_station.txt`.

Calculates **temperature stability** for each station using standard deviation.  
- Identifies the most stable and most variable stations.  
- Writes results to `temperature_stability_stations.txt`.

### main.py
Acts as the main controller of the program.  
- Loads all CSV data using `data_utils.py`.  
- Calls seasonal, range, and stability analysis functions in order.  
- Serves as the program’s entry point.

---

## TEMPERATURES FOLDER
The `temperatures/` folder contains all input CSV files used for analysis.  
- Each CSV file should contain a `STATION_NAME` column and one column for each month (`January` to `December`).  
- CSVs are combined automatically by the program.

---

## OUTPUT FILES
The program generates three output files:

- `average_temp.txt` – Seasonal average temperatures for all stations  
- `largest_temp_range_station.txt` – Station(s) with the largest temperature range  
- `temperature_stability_stations.txt` – Most stable and most variable stations  

These files are created in the same directory as `main.py`.

---

## KEY PYTHON CONCEPTS USED
- Pandas for CSV reading, data cleaning, and aggregation  
- NumPy for numerical calculations (mean, standard deviation, max/min)  
- File handling using context managers  
- Modular program structure  
- Type hints and defensive programming (handling missing values)  

---

## HOW TO RUN
1. Ensure all files and folders are in the same directory.  
2. Place input CSV files in the `temperatures/` folder.  
3. Run the program using:

```bash
python main.py

