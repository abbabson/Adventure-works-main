import os
import csv


def escape_quotes(value):
    """ Escapes single quotes within a value by doubling them"""
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

            # Create a results folder if it does not exists
            os.makedirs('results', exist_ok=True)

            # Update the SQL file path to include the results folder
            sql_file = os.path.join('results', sql_file)

            # Create the SQL file for writing
            with open(sql_file, 'w') as sqlfile:
                # Iterate over the CSV rows
                for row in reader:
                    # Prepare the values for the insert statement
                    values = ', '.join(
                        f"'{escape_quotes(value)}'" for value in row)

                    # Generate the SQL insert statement
                    sql_insert = f"INSERT INTO {table_name} ({columns}) VALUES ({values});\n"

                    # Write the SQL insert statement to the SQL file
                    sqlfile.write(sql_insert)

                print(
                    f"Conversion completed successfully. SQL file '{sql_file}' generated.")

    except FileNotFoundError:
        print("The specified CSV file does not exist.")

    except Exception as e:
        print(f"An error occurred during the conversion: {str(e)}")



# Example usage
# csv_file = "product.csv"
# sql_file = "product.sql"

# files = ["Budget.csv", "BudgetPeriod.csv", "customer.csv", "dimdate.csv",
#          "dimProductCategory.csv", "dimProductSubCategory.csv", "product.csv", "Sales.csv", "Territory.csv"]

# for file in files:
#     convert_csv_to_sql(file)
convert_csv_to_sql("product.csv")