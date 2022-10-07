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
availability = True


# web driver parameters 
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


# availability check
if driver.find_element(By.XPATH, '// span[contains(text(), "Online Ordering Unavailable")]'):
    print("Online Ordering Unavailable")
    availability = False
    message = "Online Ordering Unavailable" + "\ntime: " + time + "\norder: " + order
    SendText(key, phone, url, time, order, message)
    driver.execute_script("window.stop();")
else:
    print("Online Ordering Available")
    availability = True


if availability == True:
    try:
        print("order modal ready")
        if time == "FUTURE":
            driver.find_element(By.XPATH, '// span[contains(text(), "Schedule for later")]').click()
        elif time == "ASAP":
            driver.find_element(By.XPATH, '//button[@data-testid="fulfillment-selector-submit"]').click()
    except TimeoutException:
        print("order modal timeout")


# menu page
try:
    print("menu page ready")
    driver.find_element(By.XPATH, '// span[contains(text(), "%s")]' % order).click()
except TimeoutException:
    print("menu page timeout")


# confirmation text
message = "Online Ordering Placed" + "\ntime: " + time + "\norder: " + order
SendText(key, phone, url, time, order, message)
print("Done")