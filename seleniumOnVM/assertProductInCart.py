import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

from seleniumOnLM.loginTest import email, password

edge_options = Options()
capabilities = webdriver.DesiredCapabilities.EDGE.copy()
capabilities['platform'] = "WINDOWS"

url = "http://localhost:4444/wd/hub"
driver = webdriver.Remote(command_executor=url, options=edge_options)


def run_test_on_edge2():
    expectedProductsList = ["Health Book", "Smartphone", "Blue Jeans"]
    actualProductsList = []

    driver.get("https://demowebshop.tricentis.com/")

    # Login
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#Password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    # Assert products in shopping cart
    driver.find_element(By.LINK_TEXT, "Shopping cart").click()
    time.sleep(3)
    cartProducts = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(3) a")

    time.sleep(7)
    for cartProduct in cartProducts:
        product_name = cartProduct.text
        actualProductsList.append(product_name)

    print("Actual Products in Cart:", actualProductsList)

    assert expectedProductsList == actualProductsList, "Expected products do not match actual products in cart."

    driver.quit()
