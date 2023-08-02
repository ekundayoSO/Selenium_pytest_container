from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utility.Generic import random_email, random_password


def run_test_on_chrome():
    service_obj = Service("/Users/omowu/Desktop/Selenium/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()

    driver.get("https://demowebshop.tricentis.com/")

    # Register new user account
    driver.find_element(By.CSS_SELECTOR, ".ico-register").click()
    driver.find_element(By.XPATH, "(//input[@type='radio'])[2]").click()
    driver.find_element(By.CSS_SELECTOR, "#FirstName").send_keys("Caroline")
    driver.find_element(By.CSS_SELECTOR, "#LastName").send_keys("West")
    driver.find_element(By.ID, "Email").send_keys(random_email)
    driver.find_element(By.ID, "Password").send_keys(random_password)
    driver.find_element(By.ID, "ConfirmPassword").send_keys(random_password)
    driver.find_element(By.ID, "register-button").click()

    expectedMsg = "Your registration"
    message = driver.find_element(By.CLASS_NAME, "result").text
    assert expectedMsg in message

    driver.close()
