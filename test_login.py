from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
  driver = webdriver.Chrome()  
  driver.get("https://www.facebook.com/")

  email_field = driver.find_element(By.ID, "email")
  password_field = driver.find_element(By.ID, "pass")
  login_button = driver.find_element(By.NAME, "login")

  email_field.send_keys("facebook_email")  
  password_field.send_keys("facebook_password")  
  login_button.click()

  time.sleep(5)  

    assert "facebook.com/home.php" in driver.current_url  

  driver.quit()

def test_invalid_login():
  driver = webdriver.Chrome()
  driver.get("https://www.facebook.com/")

  email_field = driver.find_element(By.ID, "email")
  password_field = driver.find_element(By.ID, "pass")
  login_button = driver.find_element(By.NAME, "login")

  email_field.send_keys("invalid_email@example.com")  
  password_field.send_keys("invalid_password")  
  login_button.click()

  time.sleep(5)

  error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'The password that you\'ve entered is incorrect.')]")  
  assert error_message.is_displayed()

  driver.quit()
