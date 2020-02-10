from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Projects_django\sel\chromedriver\chromedriver.exe")

driver.get("https://www.geeksforgeeks.org/")

links = driver.find_elements(By.TAG_NAME, 'a')
i = 0

for lk in links:
    if i > 10:
        break
    i += 1
    print(lk.text)