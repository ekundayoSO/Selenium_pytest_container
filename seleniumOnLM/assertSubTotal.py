from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from seleniumOnLM.loginTest import email, password


def run_test_on_firefox2():
    # Instantiate browser and navigate to URL
    firefox_options = Options()
    capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
    capabilities['platform'] = "WINDOWS"

    url = "http://localhost:4444/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=firefox_options)
    driver.implicitly_wait(5)

    driver.get("https://demowebshop.tricentis.com/")

    # Login
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#Password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    # Assert products in shopping cart
    driver.find_element(By.LINK_TEXT, "Shopping cart").click()
    prices = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(6)")

    summation = 0

    for price in prices:
        summation = summation + float(price.text)

    print(summation)
    subTotal = float(driver.find_element(By.CLASS_NAME, "product-price").text)

    assert summation == subTotal, "Summation and subTotal are equal"

    driver.close()
