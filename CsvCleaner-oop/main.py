import pandas as pd 
import os, json

class CSVTool:
    def __init__(self,filepath):
        self.__filepath = filepath
        self.__df = None
        self.summary_dict = None
    #file loading
    def load(self):
        if os.path.exists(self.__filepath):
            self.__df = pd.read_csv(self.__filepath)
            print("File loaded Successfully!")
        else:
            print("Failed! (File Not Found)")
    #Cleaning Methods
    def get_data(self):
        return self.__df
    
    def drop_duplicates(self):
        before = len(self.__df)
        self.__df.drop_duplicates(inplace=True)
        print(f"Removed {before - len(self.__df)} Duplicates!")

    def handle_missing(self, method='drop'):
        if method == 'drop':
            self.__df.dropna(inplace=True)
            print("Dropped Missing Values")
        elif method == 'fill':
            self.__df.fillna(0, inplace=True)
            print("Filling missing values with 0")

    #Summary
    def summary(self):
        if self.__df is not None:
            if self.__df.empty:
                print("No data after cleaning!")
                return
        
        rows = self.__df.shape[0]
        average = self.__df.mean(numeric_only=True).round(2)
        minimum = self.__df.min(numeric_only=True)
        maximum = self.__df.max(numeric_only=True)
        #optional
        city = self.__df['city'].value_counts() if 'city' in self.__df.columns else None
        age = self.__df['age'].value_counts(normalize=True) if 'age' in self.__df.columns else None
        gender = self.__df['gender'].value_counts() if 'gender' in self.__df.columns else None

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
        #summary dict
        summary_data = {
            "rows": rows,
            "average": average,
            "minimum": minimum,
            "maximum": maximum.to_dict()
    }
        if city is not None:
            summary_data["city"] = city.to_dict()
        if age is not None:
            summary_data["age"] = age.to_dict()
        if gender is not None:
            summary_data["gender"] = gender.to_dict()
        self.summary_dict = summary_data
    #file save
    def save(self, output_csv= 'cleaned.csv', output_json= 'cleaned.json'):
        self.__df.to_csv(output_csv, index=False)
        self.__df.to_json(output_json, orient='records', indent=4)
        print("File saved as 'cleaned.csv' and 'cleaned.json'")
    
    def save_summary(self, output_json= 'summary.json'):
        with open(output_json, 'w') as f:
            json.dump(self.summary_dict, f, indent=4)
        print("Summary saved as 'summary.json'")