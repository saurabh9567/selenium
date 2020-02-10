from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="D:\Projects_django\sel\chromedriver\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

time.sleep(5)

# driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()