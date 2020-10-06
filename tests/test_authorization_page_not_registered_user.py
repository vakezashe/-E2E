from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from e2e import authorization_page_not_registered_user as apn
import pytest
# import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from e2e import users_pom
# import requests


def test_connection():
    ''' Check connect.'''

    url = 'https://www.sbzend.ssls.com/'
    # assert apn.wdriver().get(url).status_code == 200
    # assert requests.get(url).status_code == 200
    # assert "No results found." not in driver.page_source
    print(apn.wdriver().page_source)
    print(apn.wdriver().title)
#
# def test_login_error():
#     ''' Check current page and message error. '''
#
#     url = 'https://www.sbzend.ssls.com/authorize'
#     assert requests.get(url).status_code == 200
#
#     correct_error = 'Uh oh! Email or password is incorrect'
#     incorrect_error = 'OH UH! Email or Password is Correct'
#
#     received_messages = apn.error(driver=apn.wdriver())
#
#     received_error = received_messages[0]
#     title = received_messages[1]
#     current_url = received_messages[2]
#
#     assert received_error == correct_error and received_error != incorrect_error
#     assert title == 'Sign In | SSLs.com' and current_url == 'https://www.sbzend.ssls.com/authorize'
#
