#run_test.py
# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from devices.device_config import device_configs
from time import sleep


def appium_start_session():
    options = AppiumOptions()
    options.load_capabilities(device_configs["iPhone 12"])
    base_url = "http://127.0.0.1:4723"

    driver = webdriver.Remote(base_url, options=options)
    sleep(3)
    return driver  # Return the driver directly instead of yielding



# Use the generator context to ensure driver starts and quits correctly
# session = appium_start_session()
# driver = next(session)  # Advances the generator to yield driver

# Close the session
# next(session, None)  # Advances to driver.quit() and stops the generator


