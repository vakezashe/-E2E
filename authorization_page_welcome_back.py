from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import users_pom
import authorization_page_not_registered_user


def go_to_profile(driver):
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="btn block primary"]'))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='ssls-dropdown ssls-header-user ssls-header-dropdown']"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/user/profile']"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='text ng-binding']")))


def main(user, driver):
    authorization_page_not_registered_user.login_user(user, driver)
    go_to_profile(driver)


if __name__ == "__main__":
    main(user='correct_user', driver=authorization_page_not_registered_user.wdriver())














