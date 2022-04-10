from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

services = Service(executable_path="")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=services, options=options)

driver.get(url="https://python.org/")

event_time = driver.find_elements(by=By.CSS_SELECTOR, value=".menu li time")
event_name = driver.find_elements(by=By.CSS_SELECTOR, value=".menu li a")
events_dict = {}
for i in range(len(event_time)):
    events_dict[i] = {
        "time": event_time[i].text,
        "name": event_name[i].text
    }
print(events_dict)
driver.close()