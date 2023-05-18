import csv
import os

def escape_quotes(value):
    # Escape single quotes within a value by doubling them
    return value.replace("'", "''")

def convert_csv_to_sql(csv_file):
    try:
        # Extract table name from CSV file name
        table_name = os.path.splitext(os.path.basename(csv_file))[0].lower()
        
        # Open the CSV file for reading
        with open(csv_file, 'r') as csvfile:
            # Create a CSV reader object
            reader = csv.reader(csvfile)
            
            # Extract the header row and column names
            headers = next(reader)
            columns = ', '.join(headers)
            
            # Generate the output SQL file name
            sql_file = f"{table_name}.sql"
            
            # Create the results folder if it doesn't exist
            os.makedirs('results', exist_ok=True)
            
            # Update the SQL file path to include the results folder
            sql_file = os.path.join('results', sql_file)
            
            # Create the SQL file for writing
            with open(sql_file, 'w') as sqlfile:
          
                # Iterate over the CSV rows
                for row in reader:
                    # Prepare the values for the insert statement, escaping single quotes
                    values = []
                    for value in row:
                        if value == '':
                            # Insert NULL for blank values
                            values.append('NULL')
                        else:
                            values.append(f"'{escape_quotes(value)}'")
                    
                    # Generate the SQL insert statement
                    sql_insert = f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(values)});\n"
                    
                    # Write the SQL insert statement to the SQL file
                    sqlfile.write(sql_insert)
                    
                print(f"Conversion completed successfully. SQL file '{sql_file}' generated.")
    
    except FileNotFoundError:
        print("The specified CSV file does not exist.")
    
    except Exception as e:
        print(f"An error occurred during the conversion: {str(e)}")


# Example usage
csv_file = "Sales.csv"
convert_csv_to_sql(csv_file)
