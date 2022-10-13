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
 

# environment variables & Test data
load_dotenv()
url = os.environ.get('URL')
time = os.environ.get('ORDER_TIME')
order = os.environ.get('ORDER')
key = os.environ.get("TEXT_API_KEY")
phone = os.environ.get("PHONE")
availability = isAvailable()


# web driver parameters 
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


if availability == False:
    unavailable_message = "Online ordering is currently unavailable"
    SendText(key, phone, url, time, order, unavailable_message)
    driver.quit()
else:
# menu page
    try:
        print("menu page ready")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '// span[contains(text(), "BYO Sandwich")]').click()
        driver.find_element(By.XPATH, '// div[contains(text(), "Toasted")]').click()
        driver.find_element(By.XPATH, '// div[contains(text(), "Sweet Potato Fries")]').click()
        driver.find_element(By.XPATH, '// div[contains(text(), "Ciabatta")]').click()
        driver.find_element(By.XPATH, '// div[contains(text(), "Turkey")]').click()
        driver.find_element(By.XPATH, '// div[contains(text(), "Pepper Jack")]').click()
        driver.find_element(By.XPATH, '// div[contains(text(), "Pesto Aioli")]').click()    
    except TimeoutException:
        print("menu page timeout")


    # confirmation text
    # confirmation_message = "Online Ordering Placed" + "\ntime: " + time + "\norder: " + order
    # SendText(key, phone, url, time, order, confirmation_message)

print("Done")