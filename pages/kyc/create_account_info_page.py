#kyc/create_account_info_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.kyc.close_kyc_modal import CloseKycModal


class CrateAccountInfoPage(BasePage):
    def close_button_kyc(self):
        close_button = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeNavigationBar[`name == "Blu.KYCGetStatusView"`]/XCUIElementTypeButton[1]'))
        )
        close_button.click()




