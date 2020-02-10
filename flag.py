from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='D:\Projects_django\sel\chromedriver\chromedriver.exe')

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')

driver.maximize_window()

driver.execute_script('window.scrollBy(0,1000)', "")