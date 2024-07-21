from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")

    
    try:
        wait = WebDriverWait(driver, 5)
        cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow all cookies')]")))
        cookie_button.click()
    except:
        pass

    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "pass")
    login_button = driver.find_element(By.NAME, "login")

    email_field.send_keys("facebook_email")  
    password_field.send_keys("facebook_password")  
    login_button.click()

    time.sleep(5)  

    assert "facebook.com/home.php" in driver.current_url

    driver.quit()
