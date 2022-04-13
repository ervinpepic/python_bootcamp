from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = ""

PROMISED_UP = 8
PROMISED_DOWN = 5

TWITTER_EMAIL = ""
TWITTER_PASS = ""


class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.driver = driver
        self.down = 0
        self.up = 0
        self.services = Service(executable_path=self.driver)

    def get_internet_speed(self):
        driver = webdriver.Chrome(service=self.services)
        internet_speed_url = "https://www.speedtest.net/"
        driver.get(internet_speed_url)
        go_button = driver.find_element(by=By.CLASS_NAME, value="start-text")
        go_button.click()
        time.sleep(40)
        download_speed_tag = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upload_speed_tag = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.down = download_speed_tag.text
        self.up = upload_speed_tag.text

        # driver.quit()

    def tweet_at_provider(self):
        driver = webdriver.Chrome(service=self.services)
        twitter_url = "https://twitter.com/i/flow/login"
        driver.get(twitter_url)
        time.sleep(2)
        email_field = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        email_field.send_keys(TWITTER_EMAIL)
        next_button = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[6]')
        next_button.click()
        password_field = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(TWITTER_PASS)
        login_button = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div')
        login_button.click()
        time.sleep(5)
        create_tweet_button = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        create_tweet_button.click()
        write_tweet = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span/br')
        write_tweet.send_keys(f"Hey provider, why is my UP speed {self.up} and my down speed {self.up}? You promise me a {PROMISED_DOWN} down speed and {PROMISED_UP} up speed!")



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()