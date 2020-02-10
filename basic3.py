from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\Projects_django\sel\chromedriver\chromedriver.exe")

driver.get("https://www.facebook.com/")

un = driver.find_element_by_xpath('//input[@id="email"]')
pw = driver.find_element_by_xpath('//input[@id="pass"]')

un.send_keys('verma')
pw.send_keys('ruchi@24')


driver.find_element_by_xpath('//input[@id="u_0_b"]').click()
