import os
from dotenv import load_dotenv
import keyboard
from helpers.SendText import SendText
from helpers.isAvailable import isAvailable
from helpers.login import login
from helpers.menu import menu
from helpers.checkout import checkout

class Order():
    load_dotenv()

    def __init__(self, driver, By, WebDriverWait, EC, TimeoutException): 
        url = os.environ.get('URL')
        time = os.environ.get('ORDER_TIME')
        order = os.environ.get('ORDER_FOOD')
        phone = os.environ.get("PHONE")
        email = os.environ.get("EMAIL")
        password = os.environ.get("PASSWORD")
        availabile = isAvailable()  

        # start order modal
        try:
            print("start order ready")
            if time == 'asap':
                WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[contains(text(), "Start Order")]'))).click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Log In")]'))).click()
            elif time == 'future':
                driver.find_element(By.ID, "fulfillment_time").click()
            else:
                None
        except TimeoutException:
            print('start order modal timeout')

        # menu
        menu(driver, order, By, WebDriverWait, EC, TimeoutException, email, password)

        # checkout
        checkout(driver, By, WebDriverWait, EC, TimeoutException, phone, email, password)
    
        # confirmation text
        SendText("Online Ordering Placed" + "\ntime: " + time + "\norder: " + order)