from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from e2e import users_pom
import requests


def wdriver():
    try:
        # driver = webdriver.Firefox()
        driver = webdriver.Firefox(executable_path=r'./geckodriver')
    except:
        driver = webdriver.Firefox()
        # driver = webdriver.Firefox(executable_path=r'./geckodriver')

    driver.get('https://www.sbzend.ssls.com')
    assert requests.get('https://www.sbzend.ssls.com/').status_code == 200

    # options = Options()
    # options.set_headless()
    # assert options.headless  # Operating in headless mode
    # driver = Firefox(options=options)
    # driver.get(url)

    return driver


def login_user(user, driver):
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='ssls-toolbar__btn-text']"))).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@name="email"]'))).send_keys(users_pom.get_user(user)["email"])
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys(users_pom.get_user(user)["password"])
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="btn block primary"]'))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//span[@ng-hide="showPassword"]'))).click()


def error(driver):
    login_user(user='wrong_user', driver=driver)
    error1 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="noty_text"]'))).text

    title = driver.title  # Sign In | SSLs.com
    current_url = driver.current_url  # https://www.sbzend.ssls.com/authorize

    driver.close()

    return error1, title, current_url


if __name__ == "__main__":
    error(driver=wdriver())
