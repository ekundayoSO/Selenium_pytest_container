from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from seleniumOnLM.LoginTest import email, password


def run_test_on_edge():
    # Instantiate browser and navigate to URL
    service_obj = Service("/Users/omowu/Desktop/Selenium/msedgedriver.exe")
    driver = webdriver.Edge(service=service_obj)
    driver.maximize_window()

    driver.get("https://demowebshop.tricentis.com/")

    # Login
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#Password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    # Add products to shopping cart
    products = ["Health Book", "Smartphone", "Blue Jeans"]

    for product in products:
        search_box = driver.find_element(By.CSS_SELECTOR, "#small-searchterms")
        search_box.send_keys(product, Keys.RETURN)
        add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "input[value='Add to cart']")
        add_to_cart_button.click()

    driver.quit()
