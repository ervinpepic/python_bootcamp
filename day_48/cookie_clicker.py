from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

services = Service(executable_path="")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=services, options=options)

driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")

time.time() + 5
cookie.click()


# driver.quit()