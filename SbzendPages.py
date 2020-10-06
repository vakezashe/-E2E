from e2e.BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    BUTTON_LOG_IN = (By.XPATH, "//span[@class='ssls-toolbar__btn-text']")
    MAIL_FIELD = (By.XPATH, '//input[@name="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    PASSWORD_CHECK = (By.XPATH, '//button[@ng-click="showPassword = !showPassword"]')
    BUTTON_LOGIN = (By.XPATH, "//button[@class='btn block primary']")


class LoginPage(BasePage):

    def go_to_authorize_page(self):
        login_button = self.find_element(Locators.BUTTON_LOG_IN)
        login_button.click()

    def enter_mail(self, mail):
        field_mail = self.find_element(Locators.MAIL_FIELD)
        field_mail.clear()
        field_mail.click()
        field_mail.send_keys(mail)
        return field_mail

    def enter_password(self, password):
        field_password = self.find_element(Locators.PASSWORD_FIELD)
        field_password.click()
        field_password.send_keys(password)

        button_login = self.find_element(Locators.BUTTON_LOGIN)
        button_login.click()

        return field_password

    def check_password(self):
        button_eye = self.find_element(Locators.PASSWORD_CHECK)
        button_eye.click()



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
