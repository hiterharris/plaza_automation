def login(driver, By, WebDriverWait, EC, TimeoutException, email, password):
    try:
        print("login ready")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Log In")]'))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "phone-email-input"))).send_keys(email)
        driver.find_element(By.XPATH, '// button[contains(text(), "Continue")]').click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// input[@data-testid="enter-your-password-modal-password"]'))).send_keys(password)
        driver.find_element(By.XPATH, '// button[contains(text(), "Next")]').click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[contains(text(), "Skip")]'))).click()
    except TimeoutException:
        print("login timeout")