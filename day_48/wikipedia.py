from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

services = Service(executable_path="")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=services, options=options)

# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
driver.get(url="http://secure-retreat-92358.herokuapp.com/")

# statistic_number = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')
# statistic_number.click()

# all_portals = driver.find_element(by=By.LINK_TEXT, value="All portals")

fname = driver.find_element(by=By.NAME, value="fName")
fname.send_keys("Ervin")
lname = driver.find_element(by=By.NAME, value="lName")
lname.send_keys("Pepic")
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("ervin@ervin.com")

signup = driver.find_element(by=By.TAG_NAME, value="button")
signup.send_keys(Keys.ENTER)

# driver.quit()