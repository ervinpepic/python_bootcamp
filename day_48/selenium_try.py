from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

services = Service(executable_path="")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=services, options=options)

# driver.get(url="https://www.amazon.com/dp/B07TKNKKNC/ref=sbl_dpx_kitchen-electric-cookware_B001E5CWVU_0")
# price = driver.find_element(By.CLASS_NAME, "a-price")
# print(price.text)

driver.get(url="https://python.org/")
# search = driver.find_element(By.NAME, value="q")
# docs = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
# print(docs.text)
# print(search.tag_name)
bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)
driver.close()