from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#PATH = "C:\Users\HVALDES1\PycharmProjects\bin/chromedriver.exe"

driver = webdriver.Edge()

driver.get('https://www.swcm.ford.com/swcm/')

#element = driver.find_element(By.ID, 'sb_form_q')
#element.send_keys('WebDriver')
#element.submit()
driver.get('https://www.swcm.ford.com/swcm/')
print(driver.title)
time.sleep(5)
#search = driver.find_element(By.CSS_SELECTOR,{"[@aria-label='Active Directory']"})
time.sleep(60)
driver.quit()