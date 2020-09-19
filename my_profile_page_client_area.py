from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import users_pom
import authorization_page_welcome_back as apw
import authorization_page_not_registered_user as apn


def data_user(driver):
    user_info = {}

    name = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@ng-hide=\"activeRow === 'name'\"]"))).text
    email = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@ng-hide=\"activeRow === 'email'\"]"))).text
    phone = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@ng-hide=\"activeRow === 'phone'\"]"))).text
    address = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@ng-hide=\"activeRow === 'address'\"]"))).text

    support_pin = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@ng-class=\"{disabled: activeRow !== 'pin' && activeRow !== 'all'}\"]"))).text

    support_pin = ''.join(support_pin.split()[-1])

    newsletter = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class=\"text mail-list\"]"))).text

    user_info["name"]=name
    user_info['phone']=phone
    user_info['address']=address
    user_info['support_pin']=support_pin
    user_info['newsletter']=newsletter
    return user_info


def logout_user(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="ssls-dropdown ssls-header-user ssls-header-dropdown"]'))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, '//button[@class="ssls-btn waves-effect waves-classic ssls-header-dropdown-nav-item ssls-header-btn"]'))).click()
    driver.close()


def precondition(user, driver):
    apn.login_user(user, driver)
    apw.go_to_profile(driver)
    user_data = data_user(driver)
    logout_user(driver)
    return user_data


first_user_data = precondition(user='correct_user', driver=apn.wdriver())
second_user_data = precondition(user='correct_user', driver=apn.wdriver())

print(first_user_data)
print(second_user_data)


if __name__ == "__main__":
    assert first_user_data == second_user_data
