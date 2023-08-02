from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from seleniumOnVM.LoginTest import email, password

firefox_options = Options()
capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
capabilities['platform'] = "WINDOWS"

url = "http://localhost:4444/wd/hub"
driver = webdriver.Remote(command_executor=url, options=firefox_options)


def run_test_on_firefox():
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

    print("I'm using FIREFOX this time to run the test remotely!")

    driver.close()
