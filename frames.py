from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='D:\Projects_django\sel\chromedriver\chromedriver.exe')

driver.get('https://selenium.dev/selenium/docs/api/java/index.html')

driver.switch_to.frame('packageListFrame')

driver.find_element_by_link_text('org.openqa.selenium').click()

