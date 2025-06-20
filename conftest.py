import pytest
from selenium import webdriver

from notifications import TelegramReporter
from urls import manee


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()

    driver.get(manee)

    yield driver
    driver.quit()


def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 0:
        reporter = TelegramReporter(
            bot_token="8110887814:AAF0MXfqBpwgTCnyZYzZq9Uph5tmva14DKQ",
            chat_id="1032063128"
        )
        reporter.send_report("tests/allure-results")