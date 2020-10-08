# from SbzendPages import SearchHelper
from e2e.SbzendPages import LoginPage as lp
import time
from e2e.users_pom import get_user


def test_go_to_login_page(browser):
    main_page = lp(browser)
    main_page.go_to_site()
    time.sleep(2)
    assert browser.title.lower() in 'cheap ssl certificates—buy ssl certs $3.77 & save 52%'
    # print(browser.title.lower())

    main_page.go_to_authorize_page()
    time.sleep(2)
    # print(browser.title.lower())
    assert browser.title.lower() == 'sign in | ssls.com'

    # elements = yandex_main_page.check_navigation_bar()
    # print(elements)
    # assert "Картинки" and "Видео" in elements


def test_enter_incorrect_mail(browser, user='wrong_user'):
    login_page = lp(browser)
    login_page.enter_mail('Uh oh! This isn’t an email')
    time.sleep(2)
    assert 'Uh oh! This' and 'isn’t an email' in browser.page_source


def test_enter_wrong_mail(browser, user='wrong_user'):
    login_page = lp(browser)
    login_page.enter_mail(get_user(user)["email"])


def test_enter_wrong_password(browser, user='wrong_user'):
    login_page = lp(browser)
    login_page.enter_password(get_user(user)["password"])
    time.sleep(2)
    assert 'Uh oh! Email or password is incorrect' in browser.page_source


def test_check_password(browser):
    login_page = lp(browser)
    login_page.check_password()


def test_enter_correct_mail(browser, user='correct_user'):
    login_page = lp(browser)
    login_page.enter_mail(get_user(user)["email"])


def test_enter_correct_password(browser, user='correct_user'):
    login_page = lp(browser)
    login_page.enter_password(get_user(user)["password"])
    # time.sleep(2)
    # assert 'Uh oh! Email or password is incorrect' not in browser.page_source

