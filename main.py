import pandas as pd
import os

def clean_csv(input_file,output_csv="cleaned.csv",output_json="cleaned.json"):
    try:
        #load
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, input_file)
        df = pd.read_csv(filepath)
        
        #drop duplicates
        df = df.drop_duplicates()

        #strip spaces
        df = df.map(lambda x: x.strip() if isinstance(x,str) else x)
        
        #capatilize strings
        for col in df.select_dtypes(include="object"):
            if col != 'date':
                df[col] = df[col].str.title()
        
        #handle dates
        if 'date' in df.columns:
            df['date'] = df["date"].astype(str).str.strip()
            df['date'] = pd.to_datetime(df["date"],errors='coerce')
            #sort
            df.sort_values(by='date',inplace=True)
            #format
            df["date"] = df["date"].dt.strftime('%d-%m-%y')
        
        #save cleaned file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csvfile = os.path.join(script_dir, output_csv)
        df.to_csv(csvfile, index=False)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        jsonfile = os.path.join(script_dir, output_json)
        df.to_json(jsonfile, orient="records", indent=4)
        
        print(f"✔ File Cleaned and Saved as {output_csv} and {output_json}")
    except FileNotFoundError:
        print("❌ Input File Not Found!")
    except Exception as e:
        print(f"⚠ Error: {e}")
        
if __name__ == "__main__":
    while True:
        print("1. Clean a CSV file!")
        print("2. Enter q to quit!")
        choice = input("Choose a Number:  ")
        if choice == "1":
            file = input("Enter CSV file Name(e.g. data.csv):  ").strip()
            clean_csv(file)
        elif choice == "2":
            print("Good Bye! 👋")
            break
        else:
            print("❌ Invalid choice! Try again")
