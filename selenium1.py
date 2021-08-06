# Selenium Tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver

#PATH = "C:\Program Files (x86)"
#driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)/chromedriver.exe') #this line fixes permission errors

driver.get("https://balazs-balint.netlify.app/")

print(driver.title) # gets the title of the webpage
