from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

from utility.Generic import reused_info

email, password = reused_info()


def run_test_on_firefox():
    # Instantiate browser and navigate to URL
    service_obj = Service("/Users/omowu/Desktop/Selenium/geckodriver.exe")
    driver = webdriver.Firefox(service=service_obj)
    driver.minimize_window()

    driver.get("https://demowebshop.tricentis.com/")

    # Login
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#Password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    print(driver.find_element(By.CLASS_NAME, "ico-logout").text)

    LoginSuccess = "Log out"
    Element = driver.find_element(By.CLASS_NAME, "ico-logout").text
    assert LoginSuccess in Element

    driver.close()
