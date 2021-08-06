# Selenium Tutorial #2
# Selenium docu. on explicit waits

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)/chromedriver.exe') #this line fixes permission errors
driver.get("https://www.techwithtim.net/")

search = driver.find_element_by_name("s") #we are accessing the seach field on Tim's site.
search.send_keys("test")    #input to the search box
search.send_keys(Keys.RETURN) #we enter our inputs

# print(driver.page_source) #we get the source code of the page (will be hard to read, if we dont format it)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text) #printing out the summaries
except:
    driver.quit()


driver.quit()
