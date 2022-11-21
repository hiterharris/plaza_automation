def menu(driver, order, drink, By, WebDriverWait, EC, TimeoutException, email, password):
    if order == 'previous':
    # order again
        try:
            print("menu - order again ready")
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[@data-testid="reorder-add-to-cart"]'))).click()
        except TimeoutException:
            print("order again timeout")
    else:
    # new order - food
        try:
            print("new order - food ready")
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "BYO Sandwich")]'))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[@aria-label="Toasted"]'))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Sweet Potato Fries")]'))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Ciabatta")]'))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Turkey")]'))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Pepper Jack")]'))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Pesto Aioli")]'))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Add to Cart")]'))).click()
        except TimeoutException:
            print("new order - food timeout")
    # new order - drink
        try:
            print("new order - drink ready")
            if drink == 'fountain':
                WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Fountain Soda, Tea")]'))).click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Add to Cart")]'))).click()
            elif drink == 'water':
                WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Dasani, Perrier, Vitamin Water")]'))).click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Add to Cart")]'))).click()
            else:
                None
        except TimeoutException:
            print("new order - drink timeout")