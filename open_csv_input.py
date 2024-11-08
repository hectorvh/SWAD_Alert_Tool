import csv

import csv
import os

def csv_to_matrix(filepath):
    """Reads a CSV file and returns it as a matrix."""
    list_ecu = []
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                list_ecu.append(row)
        return list_ecu
    except FileNotFoundError:
        print(f"Error: CSV file '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None


# Example Usage:  Construct the full file path correctly.
filepath = os.path.join("C:\\Users\\HVALDES1\\PycharmProjects\\SWAD_01", "List.csv")  #Use os.path.join for better path handling

list_ecu = csv_to_matrix(filepath)

#rows = matrix  #Get number of rows
#cols = matrix[0] #Get number of cols (assuming all rows have same length)

if list_ecu is not None:
    print("Table ok")
    #print(matrix[1][1])
    #for row in matrix:
    #    print(row)
elif list_ecu == []:
    print("File is empty.")