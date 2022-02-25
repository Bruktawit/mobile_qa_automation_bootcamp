from appium import webdriver


class WebCommon:
    def __init__(self, apk_name):
        self.apk_name = apk_name
        self.driver = None

    def init_driver(self):
        desired_capabilities = {
            "deviceName": "ZTE Blade 10 Smart",
            "platformName": "Android",
            "app": self.apk_name
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()
