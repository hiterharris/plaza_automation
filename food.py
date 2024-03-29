import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from helpers.SendText import SendText
from helpers.isAvailable import isAvailable
from helpers.Order import Order

# env
load_dotenv()
url = os.environ.get('URL')
drink = 'false'
headless = os.environ.get('HEADLESS')
options = Options()
availabile = isAvailable()

# web driver parameters 
if headless == 'true':
    options.headless = True
driver = webdriver.Chrome(options=options)
driver.get(url)

# start order
if WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Open")]'))):
    print("Ordering Available")
    env = 'prod'
    Order(driver, By, WebDriverWait, EC, TimeoutException, env, drink)
else:
    print("Ordering Unavailable")
    SendText("Online ordering is currently unavailable")

# end process
print("Done")
driver.quit()