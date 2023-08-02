from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

from utility.Generic import reused_info

email, password = reused_info()

edge_options = Options()
capabilities = webdriver.DesiredCapabilities.EDGE.copy()
capabilities['platform'] = "WINDOWS"

url = "http://localhost:4444/wd/hub"
driver = webdriver.Remote(command_executor=url, options=edge_options)


def run_test_on_edge():
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

    print("EDGE is live remotely!")


    driver.close()
