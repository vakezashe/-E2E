# from SbzendPages import SearchHelper
from e2e.SbzendPages import LoginPage as lp
import time
from e2e.users_pom import get_user


def test_go_to_login_page(browser):

    main_page = lp(browser)

    main_page.go_to_site()
    assert browser.title.lower() in 'cheap ssl certificates—buy ssl certs $3.77 & save 52%'
    # print(browser.title.lower())

    main_page.go_to_authorize_page()
    time.sleep(2)
    # print(browser.title.lower())
    assert browser.title.lower() == 'sign in | ssls.com'

    # yandex_main_page.enter_word("Hello")
    # yandex_main_page.enter_word("Python")
    # main_page.enter_word("Python")

    # yandex_main_page.click_on_the_search_button()
    # main_page.click_on_the_search_button()

    # elements = yandex_main_page.check_navigation_bar()
    # print(elements)

    # assert "Картинки" and "Видео" in elements


def test_enter_mail(browser, user='wrong_user'):
    login_page = lp(browser)
    login_page.enter_mail(get_user(user)["email"])







