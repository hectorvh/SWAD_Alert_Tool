from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

import open_csv_input

#connection webdriver
try:
    # Initialize the webdriver
    driver = webdriver.Edge()

    # Navigate to the URL (replace with your actual URL)
    driver.get("https://www.swcm.ford.com/healthchart")

    # Explicit wait to ensure the element is present before searching
    timeout = 10  # seconds
    try:
        # Find the button using aria-label and press it
        button = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Active Directory']"))
        )
        button.click()

        print("Active Directory button found and clicked!")
        #Has succesfully logined to healthchart page
        time.sleep(10)
        """ECU_field = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Active Directory']"))
        )
        ECU_field = driver.find_element(By.ID, "colum-ecu-filer")  # Replace with actual ID
        ECU_field.send_keys("RGTM")"""
        rows = len(open_csv_input.list_ecu)  # Get number of rows
        #cols = len(open_csv_input.list_ecu)  # Get number of cols (assuming all rows have same length)
        print(f"number of rows {rows}")
        #for i in range(rows):
        ecu_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@type='text' and contains(@class, 'inputwidth')]"))
        )
        for j in range(1,rows):
            try:
                ecu_input.clear()
                current_ecu = open_csv_input.list_ecu[j][1]
                print(f"matrix ECU {current_ecu}")
                ecu_input.send_keys(current_ecu)
                print(f"Entered: {ecu_input} at ({j}, {1})")
                time.sleep(1)  # Add a small delay to avoid issues with fast typing. Adjust as needed.

            except Exception as e:
                print(f"Error at ({1}, {j}): {e}")  # Handle exceptions gracefully"""

        print("Text on csv entered successfully!")

        time.sleep(10)
    except TimeoutException:
        print("Active Directory button not found within the timeout period.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()