#kyc/close_kyc_modal.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class CloseKycModal(BasePage):
    def close_kyc_modal_title(self):
        close_kyc_modal_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'خروج از فرایند'))
        )
        print(close_kyc_modal_title.get_attribute("name"))
        return close_kyc_modal_title.get_attribute("name")

    def close_kyc_modal_description(self):
        close_kyc_modal_description = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'خروج از فرایند'))
        )
        print(close_kyc_modal_description.get_attribute('name'))
        return close_kyc_modal_description.get_attribute('name')

    def close_kyc_modal_cancel_button_text(self):
        close_kyc_modal_cancel_button_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "انصراف"`]'))
        )
        print(close_kyc_modal_cancel_button_text.get_attribute('name'))
        return close_kyc_modal_cancel_button_text.get_attribute('name')

    def close_kyc_modal_cancel_button(self):
        close_kyc_modal_cancel_button_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "انصراف"`]'))
        )
        close_kyc_modal_cancel_button_text.click()

    def close_kyc_modal_exit_button_text(self):
        close_kyc_modal_exit_button_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "خارج شدن"`]'))
        )
        print(close_kyc_modal_exit_button_text.get_attribute('name'))
        return close_kyc_modal_exit_button_text.get_attribute('name')

    def close_kyc_modal_exit_button(self):
        close_kyc_modal_exit_button = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "خارج شدن"`]'))
        )
        close_kyc_modal_exit_button.click()