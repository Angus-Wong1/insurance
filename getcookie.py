import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle


driver = selenium.webdriver.Firefox()
driver.get('https://www.cms.gov/medicare/physician-fee-schedule/search')
time.sleep(5)
with open('cookies.pkl', 'wb') as f:

    pickle.dump(driver.get_cookies(),f)


print(driver.get_cookies())

driver.quit()
