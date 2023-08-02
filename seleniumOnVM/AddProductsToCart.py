from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from seleniumOnVM.LoginTest import email, password

chrome_options = Options()
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
capabilities['platform'] = "WINDOWS"

url = "http://localhost:4444/wd/hub"
driver = webdriver.Remote(command_executor=url, options=chrome_options)


def run_test_on_chrome():
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

    print("I'm running this test remotely on CHROME")

    driver.quit()
