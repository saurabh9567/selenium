from selenium import webdriver
import os

class RunChromeTestsWindows():
    def test(self):
        driverloc = "D:\\Projects_django\\sel\\chromedriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverloc
        driver = webdriver.Chrome(driverloc)
        driver.get("https://learn.letskodeit.com/p/practice")
        # driver = webdriver.Chrome()
        # driver.get("https://learn.letskodeit.com/p/practice")


chromeTest = RunChromeTestsWindows()
chromeTest.test()