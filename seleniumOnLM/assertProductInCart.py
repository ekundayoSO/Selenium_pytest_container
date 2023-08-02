from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from seleniumOnLM.loginTest import email, password


def run_test_on_edge2():
    expectedProductsList = ["Health Book", "Smartphone", "Blue Jeans"]
    actualProductsList = []

    # Instantiate browser and navigate to URL
    service_obj = Service("/Users/omowu/Desktop/Selenium/msedgedriver.exe")
    driver = webdriver.Edge(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://demowebshop.tricentis.com/")

    # Login
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#Password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    # Assert products in shopping cart
    driver.find_element(By.LINK_TEXT, "Shopping cart").click()
    cartProducts = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(3) a")

    for cartProduct in cartProducts:
        product_names = cartProduct.text
        actualProductsList.append(product_names)
        print("My product names", product_names)

    print("Actual Products in Cart:", actualProductsList)

    assert expectedProductsList == actualProductsList, "Expected products do not match actual products in cart."

    driver.quit()
