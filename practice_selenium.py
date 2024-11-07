from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

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
        ecu_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and contains(@class, 'inputwidth')]"))
        )

        # Clear the existing text in the input field
        ecu_input.clear()

        # Send the text "RGTM" to the input field
        ecu_input.send_keys("RGTM")

        print("Text 'RGTM' entered successfully!")

        time.sleep(10)
    except TimeoutException:
        print("Active Directory button not found within the timeout period.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()