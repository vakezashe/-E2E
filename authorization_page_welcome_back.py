from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from e2e import users_pom
from e2e import authorization_page_not_registered_user as apn


def go_to_profile(driver):
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="btn block primary"]'))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='ssls-dropdown ssls-header-user ssls-header-dropdown']"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/user/profile']"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='text ng-binding']")))


def main(user, driver):
    apn.login_user(user, driver)
    go_to_profile(driver)

    current_url = driver.current_url  # https://www.sbzend.ssls.com/user/profile
    title = driver.title  # My SSL

    driver.close()

    return current_url, title


if __name__ == "__main__":
    main(user='correct_user', driver=apn.wdriver())

