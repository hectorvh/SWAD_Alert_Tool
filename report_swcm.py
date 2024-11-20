from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.options import Options
import time
import os
import glob
import zipfile
import open_csv_input
from count_rows import populated_rows

#set download folder
download_dir = r"C:\Users\HVALDES1\PycharmProjects\SWAD_01"
edge_options = Options()
#edge_options.add_argument("--start-minimized")  # Minimize at startup
edge_options.add_experimental_option('prefs', {
    'download.default_directory': download_dir  # Change this to your desired path
})
#Options.add_argument("--start-minimized") #this works well on Windows
#connection webdriver
try:
    # Initialize the webdriver
    driver = webdriver.Edge(options=edge_options)

    # Navigate to the URL (replace with your actual URL)
    driver.get("https://www.swcm.ford.com/healthchart")

    # Explicit wait to ensure the element is present before searching
    timeout = 20  # seconds
    #driver.maximize_window()
    driver.minimize_window()
    zoom_level = .7
    driver.execute_script(f"document.body.style.zoom = '{zoom_level}';")

    try:
        # Find the button Active Directory, using aria-label and press it
        button = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Active Directory']"))
        )
        button.click()
        # Has succesfully logined to healthchart page
        print("Active Directory button found and clicked!")
        time.sleep(8)
    except TimeoutException:
        print("Active Directory button not found within the timeout period.")

    #select the specific view
    #select menu of view and click to dropdown
    '''dropdown_view = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".view-selection-dropdown.ng-select"))
    )
    if "ng-select-opened" not in dropdown_view.get_attribute("class"):
        dropdown_view.click()
        print("Dropdown found and clicked!")
    time.sleep(5)

    #select 6 aye view
    option_view = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='6 eyes View']"))
    )
    option_view.click()
    time.sleep(2)'''

    # insert programs strings
    rows = len(open_csv_input.list_ecu)  # Get number of rows
    #rows = count_rows.populated_rows  # Get number of rows
    #rows = populated_rows.count_populated_rows
    print(f"Number of programs {rows-1}")

    zoom_level = .7
    driver.execute_script(f"document.body.style.zoom = '{zoom_level}';")
    program_input = driver.find_element("xpath", "//th[contains(@class, 'affectedPrograms')]//descendant::input")
    #program_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'affectedPrograms')]")))
    for j in range(1,rows):
        try:
            if open_csv_input.list_ecu[j][0] is not None and open_csv_input.list_ecu[j][0].strip(): #open_csv_input.list_ecu[j][0] is not None:
                program_input.click()
                program_input.clear()
                current_ecu = open_csv_input.list_ecu[j][0]
                print(f"Downloading ECU {current_ecu}")
                program_input.send_keys(current_ecu)
                print(f"Entered: {program_input} at ({j}, {0})")
                time.sleep(2)  # Add a small delay to avoid issues with fast typing. Adjust as needed.

                # select Export Report menu
                # select menu of view and click to dropdown
                dropdown_export = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "a.export-report"))
                )
                #if "ng-select-opened" not in dropdown_export.get_attribute("class"):
                dropdown_export.click()
                time.sleep(2)

                # select export as Excel
                option_export = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Export as Excel')]"))  # Adjust XPath as needed
                )
                option_export.click()
                time.sleep(10)


        except Exception as e:
            print(f"Error at ({j}): {e}")  # Handle exceptions gracefully"""

    print("Zip folders donwloaded succesfully!")

    time.sleep(15)

    print(f"The number of populated rows is: {populated_rows}")
    files = glob.glob(os.path.join(download_dir, "*.zip"))
    files.sort(key=os.path.getctime, reverse=True)  # Sort by creation time, newest first
    for i in range(1, populated_rows+1):
        # Get a list of all files in the download directory
        latest_file = files[:i]

    print("The latest downloaded file is:", latest_file)

    for zip_file_path in latest_file:
        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(download_dir)  # Consider specifying a different extraction directory to avoid overwriting.
                print(f"Extracted: {zip_file_path}")
            os.remove(zip_file_path)  # Delete the .zip file after extraction
            print(f"Deleted: {zip_file_path}")
        except (zipfile.BadZipFile, FileNotFoundError) as e:
            print(f"Error processing {zip_file_path}: {e}")

    files_xlsx = glob.glob(os.path.join(download_dir, "*.xlsx"))
    files_xlsx.sort(key=os.path.getctime, reverse=True)  # Sort by creation time, newest first
    for i in range(1, populated_rows + 1):
        # Get a list of all files in the download directory
        latest_file_xlsx = files_xlsx[:i]
        print(latest_file_xlsx)
    txt_file_path = os.path.join(download_dir, 'temp.txt')

    with open(txt_file_path, 'w', encoding='utf-8') as file:
        for element in latest_file_xlsx:
            # Write the element followed by a newline character to the file
            file.write(element + '\n')

    print(f"The list has been saved to '{txt_file_path}'.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()


