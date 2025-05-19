from selenium.common import TimeoutException, InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import manee


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = manee

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def open_page(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator))
            )
            return element
        except TimeoutException:
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return None


    def click_to_element(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def input_value(self, value: str, locator: tuple) -> None:
        """Вводит значение в указанное поле"""
        try:
            how, what = locator
            element = self.wait.until(EC.element_to_be_clickable((how, what)))
            element.click()  # Фокус на элемент перед вводом
            element.clear()
            element.send_keys(value)
        except TimeoutException:
            raise AssertionError(f"Элемент '{what}' не найден за {self.wait.timeout} сек")
        except InvalidElementStateException as e:
            raise AssertionError(f"Нельзя взаимодействовать с элементом '{what}': {str(e)}")

    def click(self, how: str, what: str) -> None:
        """Метод клик по элементу.

        :Args:
         - how - обращение к локатору
         - what - локтор

        """
        try:
            element = self.wait.until(EC.element_to_be_clickable((how, what)))
            element.click()
        except Exception as e:
            assert (
                e == TimeoutException
            ), f"Ошибка\nЛокатор: '{what}' при клике по элементу - не найден"

    def input_execute_scrip(self, value: str, how: str, what: str) -> None:
        """Метод ввода через JS.

        :Args:
         - value - нужное значение
         - how - обращение к локатору
         - what - локтор

        """
        try:
            element = self.wait.until(EC.element_to_be_clickable((how, what)))
            element.click()
            self.driver.execute_script('arguments[0].value = "";', element)
            element.send_keys(value)
        except Exception as e:
            assert (
                e == TimeoutException
            ), f"Ошибка\nЛокатор: '{what}' ввода значения в поле- не найден"


