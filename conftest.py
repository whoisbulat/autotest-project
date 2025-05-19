import pytest
from selenium import webdriver

from urls import manee


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()

    driver.get(manee)

    yield driver
    driver.quit()