# CSV Cleaner OOP

A simple Python tool for cleaning and summarizing CSV files using an object-oriented approach.

## Features
- Load CSV files
- Drop duplicates and handle missing values (drop or fill with 0)
- Generate quick data summaries (rows, averages, min/max, value counts)
- Save cleaned data to CSV/JSON
- Save summary to JSON

## Requirements
- Python 3.x
- pandas

Install dependencies:
```
pip install pandas
```

## Usage
1. Place your CSV file in the project directory.
2. Update the file path in your script when creating a `CSVTool` object.
3. Use the provided methods to clean, summarize, and save your data.

Example:
```python
from main import CSVTool

tool = CSVTool('yourfile.csv')
tool.load()
tool.drop_duplicates()
tool.handle_missing('fill')
tool.summary()
tool.save()
tool.save_summary()
```
