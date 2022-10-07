import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import keyboard
from SendText import SendText


# environment variables & Test data
load_dotenv()
url = os.environ.get('URL')
time = os.environ.get('TIME')
order = os.environ.get('ORDER')
key = os.environ.get("TEXT_API_KEY")
phone = os.environ.get("PHONE")


# web driver parameters 
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


# availability check
try:
    driver.implicitly_wait(10)
    if driver.find_element(By.XPATH, '// span[contains(text(), "Online Ordering Unavailable")]'):
        message = "Online Ordering Unavailable" + "\ntime: " + time + "\norder: " + order
        SendText(key, phone, url, time, order, message)
        driver.execute_script("window.stop();")
    else:
        print("Online Ordering Available")
except TimeoutException:
    print("availability check timeout")


# order for pickup modal
try:
    print("order modal ready")
    if time == "FUTURE":
        driver.find_element(By.XPATH, '// span[contains(text(), "Schedule for later")]').click()
    elif time == "ASAP":
        driver.find_element(By.XPATH, '//button[@data-testid="fulfillment-selector-submit"]').click()
    else:
        pass
except TimeoutException:
    print("order modal timeout")


# menu page
try:
    print("menu page ready")
    print('order: ', order)
    driver.find_element(By.XPATH, '// span[contains(text(), "BYO Sandwich")]').click()
except TimeoutException:
    print("menu page timeout")


# confirmation text
message = "Online Ordering Placed" + "\ntime: " + time + "\norder: " + order
SendText(key, phone, url, time, order, message)
print("Done")