import pandas as pd
import os,json

def clean_csv(input_file,output_csv="cleaned.csv",output_json="cleaned.json"):
        # Strip spaces
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

        # Replace empty strings with NaN
        df.replace('', pd.NA, inplace=True)

        # Fill missing values for non-numeric columns only
        for col in df.select_dtypes(include="object"):

            import pandas as pd
            import os
            import json

            def clean_csv(input_file, output_csv="cleaned.csv", output_json="cleaned.json"):
                try:
                    # Load
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    filepath = os.path.join(script_dir, input_file)
                    df = pd.read_csv(filepath)

                    # Strip spaces
                    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

                    # Replace empty strings with NaN
                    df.replace('', pd.NA, inplace=True)

                    # Fill missing values for non-numeric columns only
                    for col in df.select_dtypes(include="object"):
                        df[col] = df[col].fillna('Missing')

                    # Capitalize strings except 'date'
                    for col in df.select_dtypes(include="object"):
                        if col != 'date':
                            df[col] = df[col].str.title()

                    # Handle dates
                    if 'date' in df.columns:
                        df['date'] = df["date"].astype(str).str.strip()
                        df['date'] = pd.to_datetime(df["date"], errors='coerce')
                        # Sort
                        df.sort_values(by='date', inplace=True)
                        # Format
                        df["date"] = df["date"].dt.strftime('%d-%m-%Y')

                    # Drop rows with missing names (optional, can comment out if not desired)
                    if 'name' in df.columns:
                        df = df[df['name'].str.lower() != 'missing']

                    # Drop duplicates only if columns exist
                    subset_cols = [col for col in ['name', 'age'] if col in df.columns]
                    if subset_cols:
                        df = df.drop_duplicates(subset=subset_cols)
                    else:
                        df = df.drop_duplicates()

                    # Convert age to numeric, set to 0 only if missing or invalid
                    if 'age' in df.columns:
                        df['age'] = pd.to_numeric(df['age'], errors='coerce')
                        df['age'] = df['age'].fillna(0).astype(int)

                    # Save cleaned file
                    csvfile = os.path.join(script_dir, output_csv)
                    df.to_csv(csvfile, index=False)
                    jsonfile = os.path.join(script_dir, output_json)
                    df.to_json(jsonfile, orient="records", indent=4)

                    print(f"✔ File Cleaned and Saved as {output_csv} and {output_json}")
                    summary(output_csv)

                except FileNotFoundError:
                    print("❌ Input File Not Found!")
                except Exception as e:
                    print(f"⚠ Error: {e}")

            def summary(input_file, output="summary.json"):
                script_dir = os.path.dirname(os.path.abspath(__file__))
                filepath = os.path.join(script_dir, input_file)
                df = pd.read_csv(filepath)
                if df.empty:
                    print("No data after cleaning!")
                    return

                rows = df.shape[0]
                average = df.mean(numeric_only=True).round(2)
                minimum = df.min(numeric_only=True)
                maximum = df.max(numeric_only=True)
                # Only calculate stats for columns that exist
                city = df['city'].value_counts() if 'city' in df.columns else None
                age = df['age'].value_counts(normalize=True).round(2) if 'age' in df.columns else None
                gender = df['gender'].value_counts() if 'gender' in df.columns else None

                print("----Quick Summary----")
                print(f"➡  Number of Rows:\n   {rows}")
                print("➡  Average values:")
                for col, val in average.items():
                    print(f"   {col}:    {val}")
                print(f"➡  Maximum Values:")
                for col, val in maximum.items():
                    print(f"   {col}:    {val}")
                print(f"➡  Minimum Values:")
                for col, val in minimum.items():
                    print(f"   {col}:    {val}")
                if age is not None:
                    print(f"➡  Age percentage:")
                    for col, val in age.items():
                        print(f"   {col}:    {val} %")
                if gender is not None:
                    print(f"➡  Genders:")
                    for col, val in gender.items():
                        print(f"   {col}:    {val}")
                if city is not None:
                    print(f"➡  People in each city")
                    for col, val in city.items():
                        print(f"   {col}:       {val}")
                print("-" * 21)

                summary_data = {
                    "rows": rows,
                    "average": average.to_dict(),
                    "minimum": minimum.to_dict(),
                    "maximum": maximum.to_dict()
                }
                if city is not None:
                    summary_data["city"] = city.to_dict()
                if age is not None:
                    summary_data["age"] = age.to_dict()
                if gender is not None:
                    summary_data["gender"] = gender.to_dict()
                summary_file = os.path.join(script_dir, output)
                with open(summary_file, "w") as f:
                    json.dump(summary_data, f, indent=4)

            if __name__ == "__main__":
                while True:
                    print("1. Clean a CSV file!")
                    print("2. Quit!")
                    choice = input("Choose a Number:  ")
                    if choice == "1":
                        file = input("Enter CSV file Name(e.g. data.csv):  ").strip()
                        clean_csv(file)
                    elif choice.lower() == "q" or choice == "2":
                        print("Good Bye! 👋")
                        break
                    else:
                        print("❌ Invalid choice! Try again")
