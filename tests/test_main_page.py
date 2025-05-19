import allure
import pytest
from data import valid_data
from locators.main_locators import MainPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPageHelper
import time



class TestMainFunctional:
    @allure.title("[Dev-1] Проверка отображения события после сохранения")
    def test_success_authorization(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_site()
        # main_page.click_register_button()
        # main_page.user_authorization(email='qwe')
        # time.sleep(2)
