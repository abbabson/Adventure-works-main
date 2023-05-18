import pandas as pd
import os 

def extract_21_columns(excel_file_path, sheet_name):
    
    

    # Read the Excel file into a Pandas DataFrame
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    # Capture only the first 21 columns
    df_21_columns = df.iloc[:, :21]

    # # Extract the file name from the provided path
    # file_name = excel_file_path.split("/")[-1].split(".")[0]

    # # Define output folder path
    # output_folder = r"C:\Users\Mrs. Edun\Documents\dumps\adventure works csv\results"

    # "Define the output CSV file path"
    # output_csv_path = output_folder + file_name + ".csv"

    # Export the DataFrame to a CSV file
    df_21_columns.to_csv("./results/products.csv", index=False)

excel_file_path = r"C:\Users\Mrs. Edun\Documents\learning PowerBI\Supercharge PowerBI\Data\Adventure Works 2020.xlsx"
sheet_name = "Products"
extract_21_columns(excel_file_path, sheet_name)