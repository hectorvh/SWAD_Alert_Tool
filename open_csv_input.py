import csv

import csv
import os

def csv_to_matrix(filepath):
    """Reads a CSV file and returns it as a matrix."""
    matrix = []
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                matrix.append(row)
        return matrix
    except FileNotFoundError:
        print(f"Error: CSV file '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None


# Example Usage:  Construct the full file path correctly.
filepath = os.path.join("C:\\Users\\HVALDES1\\PycharmProjects\\SWAD_01", "List.csv")  #Use os.path.join for better path handling

matrix = csv_to_matrix(filepath)

rows = matrix  #Get number of rows
cols = matrix[0] #Get number of cols (assuming all rows have same length)

if matrix is not None:
    print("Table data as matrix:")
    print(matrix[1][1])
    #for row in matrix:
    #    print(row)
elif matrix == []:
    print("File is empty.")