# Selenium Tutorial #3
# Page Navigating and Clicking Elements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)/chromedriver.exe') #this line fixes permission errors
driver.get("https://www.techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    #driver.back() #we go back by one Page
    #driver.foward() #we go forward

except:
    driver.quit()
