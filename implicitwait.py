from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\Projects_django\sel\chromedriver\chromedriver.exe")

driver.get("https://www.linkedin.com/")

driver.implicitly_wait(5)

driver.find_element_by_xpath('/html/body/nav/a[3]').click()

un = driver.find_element_by_xpath('//input[@id="username"]')
pw = driver.find_element_by_xpath('//input[@id="password"]')

un.send_keys('saurabhverma956@gmail.com')
pw.send_keys('ruchi@24')


driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button').click()

