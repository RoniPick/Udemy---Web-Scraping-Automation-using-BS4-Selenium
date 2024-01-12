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
NUMBER = 1
TASK_NUMBER = 1
# OP.add_argument("--headless")
OP.add_argument("--no-sandbox")  # Add this line if running in a Linux environment

DRIVER = webdriver.Chrome(options=OP)

def username(config):
    DRIVER.find_element(By.XPATH, value="//*[@id='BXP-APP']/header[1]/div/div[1]/div[2]/a[1]").click() # Find the login button, XPATH help to find any element on the page
    time.sleep(5)
    Username = DRIVER.find_element(By.ID, value="username") # Find the username field
    Username.clear()
    Username.send_keys(config["USERNAME"]) # Enter the username

def password(config):
    DRIVER.find_element(By.ID, value="login-submit").click()
    time.sleep(2)
    password = DRIVER.find_element(By.ID, value="password")
    password.clear()
    password.send_keys(config["PASSWORD"])

def create_board():
    global NUMBER  # declaring NUMBER as a global variable
    DRIVER.find_element(By.XPATH, value="//div[@class='board-tile mod-add']").click()
    time.sleep(2)
    board_name = DRIVER.find_element(By.XPATH, value="//input[contains(@class,'nch-textfield__input lsOhPsHuxEMYEb')]")
    board_name.clear()
    board_name.send_keys("Test Board " + str(NUMBER))
    NUMBER += 1 # Increment the number of boards created
    DRIVER.find_element(By.XPATH, value="//button[contains(@class,'hY6kPzdkHFJhfG bxgKMAm3lq5BpA')]").click()
    time.sleep(2)

def navigate_to_board():
    DRIVER.find_element(By.XPATH, value="//a[.='Test Board']").click()
    time.sleep(2)

def add_task():
    global TASK_NUMBER  # declaring TASK_NUMBER as a global variable
    DRIVER.find_element(By.XPATH, value="(//button[contains(@class,'O9vivwyDxMqo3q bxgKMAm3lq5BpA')])[1]").click()
    task_name = DRIVER.find_element(By.XPATH, value="//textarea[@data-testid='list-card-composer-textarea']")
    time.sleep(1)
    task_name.clear()
    task_name.send_keys("Test Task " + str(TASK_NUMBER))
    TASK_NUMBER += 1 # Increment the number of tasks created
    DRIVER.find_element(By.XPATH, value="//button[@data-testid='list-card-composer-add-card-button']").click()

def login():
    with open('config.json') as config_file:
        config = json.load(config_file)
        time.sleep(2)
        username(config)
        password(config)
        DRIVER.find_element(By.ID, value="login-submit").click()
        time.sleep(5)
        

def main():
    try:
        DRIVER.get("https://trello.com")
        login()
         # create_board()
        navigate_to_board()
        add_task()
        input("Bot operation complete. Press enter to exit.")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()

if __name__ == "__main__":
    main()
