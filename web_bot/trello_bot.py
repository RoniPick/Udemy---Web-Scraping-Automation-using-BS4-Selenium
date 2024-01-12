from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime
import os
import json

CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "chromedriver")
OP = webdriver.ChromeOptions()
# OP.add_argument("--headless")
OP.add_argument("--no-sandbox")  # Add this line if running in a Linux environment

DRIVER = webdriver.Chrome(options=OP)

def login():
    with open('config.json') as config_file:
        config = json.load(config_file)
        time.sleep(2)
        DRIVER.find_element(By.XPATH, value="//*[@id='BXP-APP']/header[1]/div/div[1]/div[2]/a[1]").click() # Find the login button, XPATH help to find any element on the page
        time.sleep(6)
        Username = DRIVER.find_element(By.ID, value="username") # Find the username field
        time.sleep(2)
        Username.clear()
        Username.send_keys(config["USERNAME"]) # Enter the username
        DRIVER.find_element(By.ID, value="login-submit").click()
        time.sleep(2)
        password = DRIVER.find_element(By.ID, value="password")
        password.clear()
        password.send_keys(config["PASSWORD"])
        DRIVER.find_element(By.ID, value="login-submit").click()
        time.sleep(5)
        


def main():
    try:
        DRIVER.get("https://trello.com")
        login()
        input("Bot operation complete. Press enter to exit.")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()

if __name__ == "__main__":
    main()
