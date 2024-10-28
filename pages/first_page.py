from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy




class FirstPage(BasePage):
    def signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "بازکردن '
                                                                      'حساب"`]'))
        )
        signup_button.click()  # Click directly without yield

    def signin_button(self):
        signin_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN,
                                           '**/XCUIElementTypeButton[`name == "حساب بلو دارم"`]'))
        )
        signin_button.click()



