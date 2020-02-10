from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\Projects_django\sel\chromedriver\chromedriver.exe")

driver.get("https://learn.letskodeit.com/p/practice")

ele = Select(driver.find_element_by_id('carselect'))

# ele.select_by_index(2)


ele.select_by_visible_text('Honda')

print(len(ele.options))

allop = ele.options

for item in allop:
    print(item.text)