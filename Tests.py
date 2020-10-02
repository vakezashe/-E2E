# from SbzendPages import SearchHelper
from e2e.SbzendPages import LoginPage as lp


def test_yandex_search(browser):

    # yandex_main_page = SearchHelper(browser)
    main_page = lp(browser)

    # yandex_main_page.go_to_site()
    main_page.go_to_site()

    # yandex_main_page.enter_word("Hello")

    # yandex_main_page.enter_word("Python")
    # main_page.enter_word("Python")

    # yandex_main_page.click_on_the_search_button()
    # main_page.click_on_the_search_button()

    # elements = yandex_main_page.check_navigation_bar()
    # print(elements)

    # assert "Картинки" and "Видео" in elements

