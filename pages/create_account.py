

el14 = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeScrollView")
el14.click()
el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="بازکردن حساب")
el15.click()
el16 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Illustrations_CompactVisual_Bank")
el16.click()
el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="در فرایند بازکردن حساب در بلو به موارد زیر نیاز خواهید داشت:")
el17.click()
el18 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Illustrations_Icons_Fast")
el18.click()
el19 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="۷ دقیقه زمان!")
el19.click()
el20 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="کمتر از ۷ دقیقه زمان نیاز دارید")
el20.click()
el21 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Illustrations_Icons_Simcard")
el21.click()
el22 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="سیم‌کارت به‌نام")
el22.click()
el23 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="فعال و به‌نام خودتان باشد")
el23.click()
el24 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Illustrations_Icons_ID_Card")
el24.click()
el25 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="اصل مدرک هویتی")
el25.click()
el26 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="[ کارت ملی هوشمند ] یا [ کد رهگیری + شناسنامه ]")
el26.click()
el27 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Illustrations_Icons_Selfie")
el27.click()
el28 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="ویدیو سلفی")
el28.click()
el29 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="کوتاه و با متن مشخص‌شده از شما ضبط خواهد شد")
el29.click()
el30 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="navigation.support.action.identifier")
el30.click()
el31 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="انصراف")
el31.click()
el32 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeNavigationBar[`name == \"Blu.KYCGetStatusView\"`]/XCUIElementTypeButton[1]")
el32.click()
el33 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Logout_Regular")
el33.click()
el34 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="خروج از فرایند")
el34.click()
el35 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="آیا می‌خواهید از فرایند خارج شوید؟")
el35.click()
el36 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeStaticText[`name == \"انصراف\"`]")
el36.click()
el37 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeNavigationBar[`name == \"Blu.KYCGetStatusView\"`]/XCUIElementTypeButton[1]")
el37.click()
el38 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeStaticText[`name == \"خارج شدن\"`]")
el38.click()
driver.execute_script('mobile:activeAppInfo')
desired_caps = driver.desired_capabilities()