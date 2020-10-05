# from BaseApp import BasePage
from e2e.BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    # LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    # LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    # LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")

    # LOCATOR_GOOGLE_SEARCH_FIELD = (By.XPATH, "//input[@class='gLFyf gsfi']")
    # LOCATOR_GOOGLE_SEARCH_BUTTON = (By.XPATH, "//input[@class='gNO89b']")

    BUTTON_LOGIN = (By.XPATH, "//span[@class='ssls-toolbar__btn-text']")
    MAIL_FIELD = (By.XPATH, '//input[@name="email"]')

    # WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.XPATH, "//span[@class='ssls-toolbar__btn-text']"))).click()


# class SearchHelper(BasePage):
class LoginPage(BasePage):

    def go_to_authorize_page(self):
        login_button = self.find_element(Locators.BUTTON_LOGIN)
        login_button.click()

    def enter_mail(self, mail):
        field_mail = self.find_element(Locators.MAIL_FIELD)
        field_mail.click()
        field_mail.send_keys(mail)
        return field_mail


        # search_field = self.find_element(Locators.BUTTON_LOGIN).click()
        # search_field.click()
        # search_field.send_keys(word)
        # return search_field

    # def enter_word(self, word):
    #     # search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
    #     search_field = self.find_element(YandexSeacrhLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
    #     search_field.click()
    #     search_field.send_keys(word)
    #     return search_field
    #
    # def click_on_the_search_button(self):
    #     # return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()
    #     return self.find_element(YandexSeacrhLocators.LOCATOR_GOOGLE_SEARCH_BUTTON, time=2).click()
    #
    # def check_navigation_bar(self):
    #     # all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
    #
    #     all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_GOOGLE_NAVIGATION_BAR, time=2)
    #
    #     # print(all_list)
    #     return all_list

        # nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        # print(nav_bar_menu)
        # return nav_bar_menu
