from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (replace with your browser's driver)
driver = webdriver.Chrome()  # Or webdriver.Firefox(), webdriver.Edge(), etc.

# Navigate to the login page
driver.get("https://your_web_portal_url/login")

# Find the username and password fields and enter your credentials
username_field = driver.find_element(By.ID, "username")  # Replace with actual ID
password_field = driver.find_element(By.ID, "password")  # Replace with actual ID
username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Click the login button
login_button = driver.find_element(By.ID, "login_button")  # Replace with actual ID
login_button.click()

# Wait for the download link to appear (adjust timeout as needed)
try:
    download_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "download_link"))  # Replace with actual ID or selector
    )
    download_link.click()

except TimeoutException:
    print("Download link not found")

# Optionally, wait for the download to complete (using OS-specific methods or libraries)
time.sleep(5)  # A crude wait; better to check the download directory

# Close the browser
driver.quit()

