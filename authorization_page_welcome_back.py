from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import users_pom
import authorization_page_not_registered_user


def main(user, driver):
    authorization_page_not_registered_user.login_user(user, driver)
    profile_data(driver)
    signout_user(driver)


def profile_data(driver):

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="btn block primary"]'))).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='ssls-dropdown ssls-header-user ssls-header-dropdown']"))).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/user/profile']"))).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='text ng-binding']")))

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

    print(name,'\n',email,'\n',phone,'\n',address,'\n',support_pin,'\n',newsletter)
    info = {}
    info["name"]=name
    info['phone']=phone
    info['address']=address
    info['support_pin']=support_pin
    info['newsletter']=newsletter
    print(info)
    return info


def signout_user(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="ssls-dropdown ssls-header-user ssls-header-dropdown"]'))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, '//button[@class="ssls-btn waves-effect waves-classic ssls-header-dropdown-nav-item ssls-header-btn"]'))).click()


if __name__ == "__main__":
    main(user='correct_user', driver=authorization_page_not_registered_user.wdriver())

