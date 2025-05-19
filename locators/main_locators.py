from selenium.webdriver.common.by import By




class MainPageLocators:
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[data-elem-id='1647594494145']")
    CONFIRM_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[data-elem-id='1647594494145']")

    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-input-lid='5786767583350']")
    NAME_INPUT = (By.CSS_SELECTOR, "[data-input-lid='5786767583351']")
    PHONE_INPUT = (By.CSS_SELECTOR, "[data-input-lid='5786767583352']")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "[data-input-lid='1702031683269']")