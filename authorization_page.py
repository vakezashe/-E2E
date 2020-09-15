from gevent import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


from e2e import users_pom

# user = 'wrong_user'
# print(users_pom.get_user(user)['email'])
# print(users_pom.get_user(user)["email"] and users_pom.get_user(user)["password"])


def routes(user):

    driver = webdriver.Firefox(executable_path=r'./geckodriver')
    driver.get('https://www.sbzend.ssls.com')

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='ssls-toolbar__btn-text']"))).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="email"]'))).send_keys(users_pom.get_user(user)["email"])

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys(users_pom.get_user(user)["password"])

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="btn block primary"]'))).click()


if __name__ == "__main__":
    routes(user='wrong_user')
