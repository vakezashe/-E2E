from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import users_pom
import requests

'''
4. "Log in" button has to be changed on "User@email" button (with dropdown menu) 

    from the left side in the Header of the page

    from the RIGHT side in the Header of the page.
'''

# user = 'wrong_user'
# print(users_pom.get_user(user)['email'])
# print(users_pom.get_user(user)["email"] and users_pom.get_user(user)["password"])


def wdriver():
    driver = webdriver.Firefox(executable_path=r'./geckodriver')
    driver.get('https://www.sbzend.ssls.com')
    assert driver.get('https://www.sbzend.ssls.com') == 200

    return driver


def routes(user, driver):
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='ssls-toolbar__btn-text']"))).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@name="email"]'))).send_keys(
        users_pom.get_user(user)["email"])

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys(
        users_pom.get_user(user)["password"])

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//span[@ng-hide="showPassword"]'))).click()

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

    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="ssls-dropdown ssls-header-user ssls-header-dropdown"]'))).click()

    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
    #     (By.XPATH, '//button[@class="ssls-btn waves-effect waves-classic ssls-header-dropdown-nav-item ssls-header-btn"]'))).click()

    # driver.close()


if __name__ == "__main__":
    routes(user='correct_user', driver=wdriver())


