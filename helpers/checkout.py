def checkout(driver, By, WebDriverWait, EC, TimeoutException, phone, email, password):
    try:
        print("checkout ready")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Continue to checkout")]'))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "phone-email-input"))).send_keys(email)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "customer_first_name"))).send_keys("Henry")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "customer_last_name"))).send_keys("Harris")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "customer_email"))).send_keys(email)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "customer_tel"))).send_keys(phone)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[contains(text(), Submit")]'))).click()
    except TimeoutException:
        print("checkout timeout")