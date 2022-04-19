import time
import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = "chromedriver"
GOOGLE_FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeBwyued13B-FTZCMSFP0hrqEkCkw6vu4N7lbc7e2NEKKrbmQ/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.50121559144775%2C%22east%22%3A-122.33333076478759%2C%22south%22%3A37.783777490767264%2C%22north%22%3A37.845616603903345%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"


headers = {
    "Accept-Language": "en-US,en;q=0.9,hr;q=0.8,sr;q=0.7,de;q=0.6,sl;q=0.5,bs;q=0.4",
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url=ZILLOW_URL, headers=headers)
html = response.text
soup = BeautifulSoup(html, "lxml")
list_links = []

try:
    links = soup.find_all(class_="list-card-link", href=True)
except TypeError:
    print("Sorry, this type is not allowed")
else:
    if not links:
        print("not found")
    else:
        for link in links:
            if "https://" not in link["href"]:
                new_link = "https://www.zillow.com" + link["href"]
                list_links.append(new_link)
            else:
                list_links.append(link["href"])
    print(list_links)

prices = soup.find_all(name="div", class_="list-card-price")
prices_list = [price.getText().strip("/mo+bd 1") for price in prices]
print(prices_list)

addresses = soup.find_all(name="address", class_="list-card-addr")
address_list = [address.getText() for address in addresses]
print(address_list)

services = Service(executable_path=CHROME_DRIVER_PATH)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=services, options=options)
driver.get(GOOGLE_FORMS_URL)

for n in range(len(list_links)):
    property = driver.find_element(by=By.CSS_SELECTOR, value='.whsOnd')
    time.sleep(2)
    property.click()
    time.sleep(2)
    property.send_keys(address_list[n])
    time.sleep(2)
    
    price = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.click()
    time.sleep(2)
    price.send_keys(prices_list[n])
    
    link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.click()
    time.sleep(2)
    link.send_keys(list_links[n])
    time.sleep(2)
    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()
    time.sleep(2)
    antoher_form = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    antoher_form.click()
    time.sleep(2)

