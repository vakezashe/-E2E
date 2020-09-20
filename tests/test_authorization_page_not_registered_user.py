from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from e2e import authorization_page_not_registered_user as apn
import pytest
import requests


def test_connection():
    ''' Проверяет соеденение.'''
    url = 'https://www.sbzend.ssls.com/'
    assert requests.get(url).status_code == 200


def test_login():
    ''' Проверяет, что находимся на странице авторищации и
    сообщение об ошибки неправильных даннах для логина  '''
    url = 'https://www.sbzend.ssls.com/authorize'
    assert requests.get(url).status_code == 200

    correct_error = 'Uh oh! Email or password is incorrect'
    incorrect_error = 'OH UH! Email or Password is Correct'

    received_error_message = apn.error(driver=apn.wdriver())

    assert received_error_message == correct_error
    assert received_error_message != incorrect_error


