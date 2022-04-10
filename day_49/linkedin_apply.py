import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

services = Service(executable_path="")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=services, options=options)

driver.get(url="https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python%20developer")

link_login = driver.find_element(by=By.LINK_TEXT, value="Sign in")
link_login.click()
time.sleep(2)
linkedin_username = driver.find_element(by=By.ID, value="username")
linkedin_username.send_keys("")
linkedin_password = driver.find_element(by=By.ID, value="password")
linkedin_password.send_keys("")
linkedin_signin_button = driver.find_element(by=By.CLASS_NAME, value="btn__primary--large")
linkedin_signin_button.click()
easy_apply = driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button")
easy_apply.click()
time.sleep(2)
apply = driver.find_element(by=By.XPATH, value='//*[@id="ember299"]')
apply.click()

