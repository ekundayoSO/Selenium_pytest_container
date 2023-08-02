from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from seleniumOnLM.LoginTest import email, password


def run_test_on_chrome2():
    service_obj = Service("/Users/omowu/Desktop/Selenium/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()

    driver.get("https://demowebshop.tricentis.com/")

    # Login
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#Password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    # Delete products in cart
    driver.find_element(By.LINK_TEXT, "Shopping cart").click()
    checkboxes = driver.find_elements(By.XPATH, "//td/input[@type='checkbox']")

    for checkbox in checkboxes:
        checkbox.click()

    driver.find_element(By.CLASS_NAME, "update-cart-button").click()

    driver.close()
