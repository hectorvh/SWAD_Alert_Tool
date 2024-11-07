import openpyxl

def excel_table_to_matrix(filepath, sheet_name="Sheet1"):
    """
    Reads a table from an Excel sheet and returns it as a matrix (list of lists).

    Args:
        filepath: Path to the Excel file.
        sheet_name: Name of the sheet containing the table (default: "Sheet1").

    Returns:
        A list of lists representing the table data, or None if an error occurs.
    """
    try:
        workbook = openpyxl.load_workbook(filepath, data_only=True)  # data_only=True to get cell values, not formulas
        sheet = workbook[sheet_name]

        matrix = []
        for row in sheet.iter_rows():
            row_data = [cell.value for cell in row]  # Extract values from cells in the row
            matrix.append(row_data)

        return matrix

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except KeyError:
        print(f"Error: Sheet '{sheet_name}' not found in the Excel file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
filepath = "your_excel_file.xlsx"  # Replace with your Excel file path
sheet_name = "YourSheetName" # Replace with your sheet name if not "Sheet1"

matrix = excel_table_to_matrix(filepath, sheet_name)

if matrix:
    print("Excel table as matrix:")
    for row in matrix:
        print(row)