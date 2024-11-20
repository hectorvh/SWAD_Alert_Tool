import csv
import os

def count_populated_rows(csv_filepath):
    """Counts populated rows in the first column of a CSV file."""
    try:
        with open(csv_filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header row (if present)
            next(reader, None)
            row_count = 0
            for row in reader:
                if row and row[0].strip():  # Check if the row is not empty and the first column is not just whitespace
                    row_count += 1
            return row_count
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_filepath}")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage:
csv_file_path = os.path.join("C:\\Users\\HVALDES1\\PycharmProjects\\SWAD_01", "List.csv")  # Replace with your CSV file path
populated_rows = count_populated_rows(csv_file_path)
#print(f"Number of populated rows in the first column: {populated_rows}")