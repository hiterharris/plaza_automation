import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import keyboard
from helpers.SendText import SendText
from helpers.isAvailable import isAvailable
from helpers.Order import Order


# env
load_dotenv()
url = os.environ.get('URL')
availabile = isAvailable()


# web driver parameters 
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


# start order
if availabile == True:
    Order(driver, By, WebDriverWait, EC, TimeoutException)
else:
    unavailable_message = "Online ordering is currently unavailable"
    SendText(unavailable_message)

print("Done")
driver.quit()