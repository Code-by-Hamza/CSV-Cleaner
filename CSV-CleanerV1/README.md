# CSV Cleaner

A simple Python script to clean and format CSV files. It removes duplicates, trims spaces, capitalizes string columns (except dates), parses and formats dates, sorts by date, and saves the cleaned data as both CSV and JSON. It also prints a quick summary and saves it as `summary.json`. Summary fields for city, age, and gender are only included if those columns exist in your CSV.


## Features
- Removes duplicate rows
- Trims leading/trailing spaces from all fields
- Capitalizes string columns (except 'date')
- Parses various date formats and standardizes them to `DD-MM-YYYY`
- Sorts data by date (if present)
- Outputs cleaned data to CSV and JSON files
- Prints and saves a quick summary of numeric columns
- If columns 'city', 'age', or 'gender' exist, their value counts are included in the summary
- Improved error handling and menu logic

## Usage
1. Run the script:
    ```bash
    python main.py
    ```
2. Follow the prompts:
    - Enter the CSV file name (e.g., `data.csv`).
    - Type `2` or `q` to quit.
3. The cleaned files will be saved as `cleaned.csv` and `cleaned.json` in the same directory. A summary will be printed and saved as `summary.json`.

## Requirements
- Python 3.10+
- pandas

Install dependencies:
```bash
pip install pandas
```

## Example
Input CSV e.g.(`sample.csv`):
```
name,age,city,gender,date
 Hamza,20,Lahore,Male,2025-09-06
Hamza,20, Lahore ,Male,2025-09-06
ali,22, Karachi,Male,2025-09-07
Ayesha ,21, Lahore,Female,2025-09-09
sara,19,islamabad,Female,2025-09-08
Ayesha,21,lahore,Female,2025-09-09
```

Output CSV (`cleaned.csv`):
```
Name,Age,City,Gender,Date
Sara,19,Islamabad,Female,09-08-2025
Hamza,20,Lahore,Male,06-09-2025
Ali,22,Karachi,Male,07-09-2025
Ayesha,21,Lahore,Female,09-09-2025
```

Quick Summary (printed and saved as `summary.json`):
```
----Quick Summary----
➡  Number of Rows:
   4
➡  Average values:
   age:    20.5
➡  Minimum Values:
   age:    19
➡  Age percentage:
   19:    0.25 %
   20:    0.25 %
   22:    0.25 %
   21:    0.25 %
➡  Genders:
   Female:    2
   Male:    2
➡  People in each city
   Lahore:       2
   Islamabad:       1
   Karachi:       1
---------------------
```
*Note: Age, gender, and city breakdowns only appear if those columns exist in your CSV.*