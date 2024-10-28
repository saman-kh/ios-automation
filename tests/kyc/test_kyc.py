from time import sleep

from pages.first_page import FirstPage
from pages.kyc.close_kyc_modal import CloseKycModal
from pages.login_page import LoginPage
from pages.select_server_bottom_sheet import SelectServerBottomSheet
from pages.kyc.create_account_info_page import CrateAccountInfoPage


from run_test import appium_start_session


def test_kyc():
    driver = appium_start_session()

    # Instantiate the FirstPage class and call signup_button()
    first_page = FirstPage(driver)
    first_page.signup_button()

    select_server_bottom_sheet = SelectServerBottomSheet(driver)
    select_server_bottom_sheet.select_uat()

    create_account_info_page = CrateAccountInfoPage(driver)
    create_account_info_page.close_button_kyc()

    # Create an instance of CloseKycModal and call close_kyc_modal_title method
    close_kyc_modal = CloseKycModal(driver)

    close_kyc_modal.close_kyc_modal_title()

    close_kyc_modal.close_kyc_modal_description()

    close_kyc_modal.close_kyc_modal_cancel_button_text()
    close_kyc_modal.close_kyc_modal_cancel_button()

    create_account_info_page.close_button_kyc()
    close_kyc_modal.close_kyc_modal_exit_button_text()
    close_kyc_modal.close_kyc_modal_exit_button()

    login_page_button = LoginPage(driver)
    login_page_button.login_page_button_text()
    login_page_button.login_page_button()

    # Close the session after the test
    sleep(2)
    driver.quit()
