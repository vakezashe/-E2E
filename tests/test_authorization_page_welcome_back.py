from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from e2e import users_pom
from e2e import authorization_page_welcome_back as apw
import pytest
import requests
from e2e.tests import test_authorization_page_not_registered_user as tapn


def test_connection():
    tapn.test_connection()


# def test_profile_page():
#     url = 'https://www.sbzend.ssls.com/user/profile'
#     print(requests.get(url).status_code)
#     print(requests.get(url).url)
#     # assert requests.get(url).status_code == 200



'''
https://www.sbzend.ssls.com/user/profile
'''


# def go_to_profile(driver):
#     WebDriverWait(driver, 5).until(
#         EC.visibility_of_element_located((By.XPATH, '//button[@class="btn block primary"]'))).click()
#     WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
#         (By.XPATH, "//div[@class='ssls-dropdown ssls-header-user ssls-header-dropdown']"))).click()
#     WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/user/profile']"))).click()
#     WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='text ng-binding']")))
#
#
# def main(user, driver):
#     authorization_page_not_registered_user.login_user(user, driver)
#     go_to_profile(driver)
#
#
# if __name__ == "__main__":
#     main(user='correct_user', driver=authorization_page_not_registered_user.wdriver())

