def login(driver, By, WebDriverWait, EC, TimeoutException, email, password):
    try:
        print("login ready")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "phone-email-input"))).send_keys(email)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[contains(text(), "Continue")]'))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// input[@data-testid="enter-your-password-modal-password"]'))).send_keys(password)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[contains(text(), "Next")]'))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[contains(text(), "Skip")]'))).click()
    except TimeoutException:
        print("login timeout")