# CSV Cleaner

A simple Python script to clean and format CSV files. It removes duplicates, trims spaces, capitalizes string columns (except dates), parses and formats dates, and saves the cleaned data as both CSV and JSON.

## Features
- Removes duplicate rows
- Trims leading/trailing spaces from all fields
- Capitalizes string columns (except 'date')
- Parses various date formats and standardizes them to `DD-MM-YY`
- Sorts data by date
- Outputs cleaned data to CSV and JSON files

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Follow the prompts to enter the CSV file name (e.g., `data.csv`).
3. The cleaned files will be saved as `cleaned.csv` and `cleaned.json` in the same directory.

## Requirements
- Python 3.10+
- pandas

Install dependencies:
```bash
pip install pandas
```

## Example
Input CSV:
```
name, age, city, date
Hamza ,20, Lahore, 2025-09-06
Ali, 22 , Karachi, 09-06-2025
```

Output CSV:
```
Name,Age,City,Date
Hamza,20,Lahore,06-09-25
Ali,22,Karachi,06-09-25
```