from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage):
    def login_page_button_text(self):
        login_page_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "حساب بلو دارم"`]'))
        )
        return login_page_button.get_attribute('name')

    def login_page_button(self):
        login_page_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "حساب بلو دارم"`]'))
        )
        login_page_button.click()
