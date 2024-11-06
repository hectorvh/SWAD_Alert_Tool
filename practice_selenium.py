from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
#PATH = "C:\Users\HVALDES1\PycharmProjects\bin/chromedriver.exe"


#driver.get('https://www.swcm.ford.com/swcm/')

#element = driver.find_element(By.ID, 'sb_form_q')
#element.send_keys('WebDriver')
#element.submit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Replace with your webdriver path

try:
    # Initialize the webdriver
    driver = webdriver.Edge()

    # Navigate to the URL (replace with your actual URL)
    driver.get("https://www.swcm.ford.com/swcm/")

    # Explicit wait to ensure the element is present before searching
    timeout = 10  # seconds
    try:
        # Find the button using aria-label
        button = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Active Directory']"))
        )

        # Click the button (optional, if you just want to verify its presence, remove this line)
        button.click()

        print("Active Directory button found and clicked!")

    except TimeoutException:
        print("Active Directory button not found within the timeout period.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()