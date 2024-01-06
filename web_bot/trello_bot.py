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

def main():
    try:
        DRIVER.get("https://trello.com")
        input("Bot operation complete. Press enter to exit.")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()

if __name__ == "__main__":
    main()
