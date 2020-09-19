from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import users_pom
import requests


def wdriver():
    driver = webdriver.Firefox(executable_path=r'./geckodriver')
    driver.get('https://www.sbzend.ssls.com')
    assert requests.get('https://www.sbzend.ssls.com/').status_code == 200
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

    # driver.close()


if __name__ == "__main__":
    login_user(user='wrong_user', driver=wdriver())
