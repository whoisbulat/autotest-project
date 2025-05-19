import time

from locators.main_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPageHelper(BasePage):
    @allure.step('Переходим на страницу стеллар бургер. Главная страница')
    def go_to_site(self):
        self.driver.get(self.base_url)

    # @allure.step('Клик по кнопке регистрации')
    # def click_register_button(self):
    #     self.click(*MainPageLocators.REGISTRATION_BUTTON)

    # @allure.step('Логин пользователя')
    # def user_authorization(self) -> None:
    #     self.click_to_element(MainPageLocators.EMAIL_INPUT)
    #     # self.click(*MainPageLocators.EMAIL_INPUT).send_keys(email)
    #     # self.input_value(email, *MainPageLocators.EMAIL_INPUT)
    #     # self.input_value(phone, *MainPageLocators.PHONE_INPUT)
    #     # if message is not None:
    #     #     self.input_value(message, *MainPageLocators.MESSAGE_INPUT)




