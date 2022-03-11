from appium import webdriver
import logging
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class WebCommon:
    def __init__(self, apk_name):
        self.apk_name = apk_name
        self.driver = None

    def init_driver(self):
        desired_capabilities = {
            "deviceName": "ZTE Blade 10 Smart",
            "platformName": "Android",
            'appPackage': '',
            'appActivity': ''
        }
        if self.apk_name == "theapp":
            desired_capabilities['appPackage'] = 'io.cloudgrey.the_app'
            desired_capabilities['appActivity'] = 'io.cloudgrey.the_app.MainActivity'
        elif self.apk_name == "filemanager":
            desired_capabilities['appPackage'] = "com.alphainventor.filemanager"
            desired_capabilities['appActivity'] = "com.alphainventor.filemanager.activity.MainActivity"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()


class Test01Android:
    @classmethod
    def setup_class(cls):
        logger.info(Test01Android.setup_class.__name__)

    @classmethod
    def teardown_class(cls):
        logger.info(Test01Android.teardown_class.__name__)

    def setup_method(self):
        logger.info(Test01Android.setup_method.__name__)

    def teardown_method(self):
        logger.info(Test01Android.teardown_method.__name__)

    # Test 01
    @pytest.mark.parametrize('os', ['android'])
    def test_01(self, request, os):
        logger.info(request.node.name)
        logger.info(os)

    # Test 02
    @pytest.mark.xfail(reason="unable to execute test")
    def test_02_xfail(self):
        assert 1 == 2

    # Test 03
    @pytest.mark.skip(reason="Unable to execute test")
    def test_03_skip(self):
        assert 1 == 2

    # Test 04
    def test_04_list_size(self):
        webcommon = WebCommon("theapp")
        webcommon.init_driver()
        driver = webcommon.get_driver()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'com.android.permissioncontroller:id/continue_button')))
        except:
            print("timeout")
            driver.quit()

        continue_element = driver.find_element(By.ID, 'com.android.permissioncontroller:id/continue_button')
        continue_element.click()

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'android:id/button1')))
        except TimeoutException:
            print("timeout")
            driver.quit()

        ok_element = driver.find_element(By.ID, 'android:id/button1')
        ok_element.click()

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//android.view.ViewGroup[@index=1]')))
        except:
            print("timeout")
            driver.quit()

        list_elements = driver.find_elements(By.XPATH,
                                             '//android.view.ViewGroup[@index=1]/android.view.ViewGroup/android.view'
                                             '.ViewGroup/android.view.ViewGroup/android.widget.TextView')

        list_length = len(list_elements)

        logger.info('List size:{' + str(list_length) + '}, expected: {7}')

        webcommon.close_driver()
        assert list_length == 7

    # Test 05
    @classmethod
    def get_element_by_text(cls, driver_test5, text_input):
        elements = driver_test5.find_elements(By.XPATH,
                                              '//android.view.ViewGroup[@index=1]/android.view.ViewGroup/android.widget.TextView')
        for element in elements:
            if element.text == text_input:
                return element

    def test_05_text(self):
        # driver for test 05
        webcommon_test5 = WebCommon("theapp")
        webcommon_test5.init_driver()
        driver_test5 = webcommon_test5.get_driver()

        try:
            WebDriverWait(driver_test5, 10).until(
                EC.presence_of_element_located((By.ID, 'com.android.permissioncontroller:id/continue_button')))
        except:
            print("timeout")
            driver_test5.quit()

        continue_element = driver_test5.find_element(By.ID, 'com.android.permissioncontroller:id/continue_button')
        continue_element.click()

        try:
            WebDriverWait(driver_test5, 10).until(EC.presence_of_element_located((By.ID, 'android:id/button1')))
        except TimeoutException:
            print("timeout")
            driver_test5.quit()

        ok_element = driver_test5.find_element(By.ID, 'android:id/button1')
        ok_element.click()

        try:
            WebDriverWait(driver_test5, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  '//android.view.ViewGroup[@index=1]')))
        except:
            print("timeout")
            driver_test5.quit()

        list_demo_element = Test01Android.get_element_by_text(driver_test5, "List Demo")
        list_demo_element.click()
        webcommon_test5.close_driver()

    # Test 06
    def test_06_send_keys(self):
        webcommon = WebCommon("theapp")
        webcommon.init_driver()
        driver = webcommon.get_driver()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'com.android.permissioncontroller:id/continue_button')))
        except:
            print("timeout")
            driver.quit()

        continue_element = driver.find_element(By.ID, 'com.android.permissioncontroller:id/continue_button')
        continue_element.click()

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'android:id/button1')))
        except TimeoutException:
            print("timeout")
            driver.quit()

        ok_element = driver.find_element(By.ID, 'android:id/button1')
        ok_element.click()

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//android.view.ViewGroup[@index=1]')))
        except:
            print("timeout")
            driver.quit()

        echo_box_item = driver.find_element(By.XPATH,
                                            '//android.view.ViewGroup[@index=1]/android.view.ViewGroup/android.widget.TextView[@text="Echo Box"]')
        echo_box_item.click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.EditText')))
        except TimeoutException:
            print("timeout ")
            driver.quit()

        text_box = driver.find_element(By.CLASS_NAME, 'android.widget.EditText')
        text_box.send_keys("Hello world")

        save_element = driver.find_element(By.CLASS_NAME, 'android.widget.TextView')
        save_element.click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@index=1]')))
        except TimeoutException:
            print("timeout ")
            driver.quit()

        saved_text = driver.find_element(By.XPATH, '//android.widget.TextView[@index=1]').text

        webcommon.close_driver()
        assert saved_text == "Hello world"

    # Test 07
    @classmethod
    def wait_and_return(cls, driver_test7):
        try:
            WebDriverWait(driver_test7, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  '//android.view.ViewGroup[@index=0]')))
        except:
            print("timeout")
            driver_test7.quit()

        list_elements = driver_test7.find_elements(By.XPATH, '//android.view.ViewGroup[@index=0]')
        return list_elements

    def test_07_wait(self):
        # driver for test 07
        webcommon_test7 = WebCommon("theapp")
        webcommon_test7.init_driver()
        driver_test7 = webcommon_test7.get_driver()

        try:
            WebDriverWait(driver_test7, 10).until(
                EC.presence_of_element_located((By.ID, 'com.android.permissioncontroller:id/continue_button')))
        except:
            print("timeout")
            driver_test7.quit()

        continue_element = driver_test7.find_element(By.ID, 'com.android.permissioncontroller:id/continue_button')
        continue_element.click()

        try:
            WebDriverWait(driver_test7, 10).until(EC.presence_of_element_located((By.ID, 'android:id/button1')))
        except TimeoutException:
            print("timeout")
            driver_test7.quit()

        ok_element = driver_test7.find_element(By.ID, 'android:id/button1')
        ok_element.click()

        try:
            WebDriverWait(driver_test7, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  '//android.view.ViewGroup[@index=1]')))
        except:
            print("timeout")
            driver_test7.quit()

        list_demo_element = driver_test7.find_element(By.XPATH,
                                                      '//android.view.ViewGroup[@index=1]/android.view.ViewGroup/android.widget.TextView[@text="List Demo"]')
        list_demo_element.click()

        list_of_elements = Test01Android.wait_and_return(driver_test7)

        elements_list = []

        i = 0
        while i < len(list_of_elements):
            elements_list.append(list_of_elements[i])
            i += 1

        webcommon_test7.close_driver()
        assert len(elements_list) != 0

    # Test 08
    @classmethod
    def scroll_method(cls, driver_test8, start_x, start_y, end_x, end_y, duration):
        driver_test8.swipe(start_x, start_y, end_x, end_y, duration)

    def test_08_scroll(self):
        # driver for test 08
        webcommon_test8 = WebCommon("theapp")
        webcommon_test8.init_driver()
        driver_test8 = webcommon_test8.get_driver()

        try:
            WebDriverWait(driver_test8, 10).until(
                EC.presence_of_element_located((By.ID, 'com.android.permissioncontroller:id/continue_button')))
        except:
            print("timeout")
            driver_test8.quit()

        continue_element = driver_test8.find_element(By.ID, 'com.android.permissioncontroller:id/continue_button')
        continue_element.click()

        try:
            WebDriverWait(driver_test8, 10).until(EC.presence_of_element_located((By.ID, 'android:id/button1')))
        except TimeoutException:
            print("timeout")
            driver_test8.quit()

        ok_element = driver_test8.find_element(By.ID, 'android:id/button1')
        ok_element.click()

        try:
            WebDriverWait(driver_test8, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  '//android.view.ViewGroup[@index=1]')))
        except:
            print("timeout")
            driver_test8.quit()

        list_demo_element = driver_test8.find_element(By.XPATH,
                                                      '//android.view.ViewGroup[@index=1]/android.view.ViewGroup/android.widget.TextView[@text="List Demo"]')
        list_demo_element.click()

        try:
            WebDriverWait(driver_test8, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  '//android.view.ViewGroup[@index=0]')))
        except:
            print("timeout")
            driver_test8.quit()

        Test01Android.scroll_method(driver_test8, 150, 1700, 150, 500, 800)

        try:
            WebDriverWait(driver_test8, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  '//android.view.ViewGroup[@index=1]')))
        except:
            print("timeout")
            driver_test8.quit()

        last_item = driver_test8.find_element(By.XPATH,
                                              '//android.view.ViewGroup[@index=1]/android.view.ViewGroup[@index=14]/android.widget.TextView')
        last_item_text = last_item.text
        webcommon_test8.close_driver()
        assert last_item_text == "Stratus"

    # Test 09
    def test_09_create_folder(self):
        os.system("adb shell mkdir /sdcard/test_folder")

        webcommon = WebCommon("filemanager")
        webcommon.init_driver()
        driver = webcommon.get_driver()

        driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//android.view.ViewGroup[@index=0]')))
        except:
            print("timeout")
            driver.quit()

        driver.find_element(By.XPATH, "//android.widget.GridView/android.widget.LinearLayout[@index=0]").click()

        # wait for list items to appear
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                            'android.widget.ListView')))
        except:
            print("timeout")
            driver.quit()

        elements = driver.find_elements(By.XPATH,
                                        '//android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')

        list_of_folder_names = []
        for element in elements:
            list_of_folder_names.append(element.text)

        driver.swipe(500, 1670, 500, 495, 400)

        elements2 = driver.find_elements(By.XPATH,
                                         '//android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')

        for element in elements2:
            if element.text not in list_of_folder_names:
                list_of_folder_names.append(element.text)

        assert "test_folder" in list_of_folder_names

        os.system("adb shell rmdir /sdcard/test_folder")
        webcommon.close_driver()

    # Test 10
    def test_10_delete_folder(self):
        # create folder
        os.system("adb shell mkdir /sdcard/test_folder")
        # delete folder
        os.system("adb shell rmdir /sdcard/test_folder")

        webcommon = WebCommon("filemanager")
        webcommon.init_driver()
        driver = webcommon.get_driver()

        driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//android.view.ViewGroup[@index=0]')))
        except:
            print("timeout")
            driver.quit()

        driver.find_element(By.XPATH, "//android.widget.GridView/android.widget.LinearLayout[@index=0]").click()

        # wait for list items to appear
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                            'android.widget.ListView')))
        except:
            print("timeout")
            driver.quit()

        elements = driver.find_elements(By.XPATH,
                                        '//android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')

        list_of_folder_names = []
        for element in elements:
            list_of_folder_names.append(element.text)

        driver.swipe(500, 1670, 500, 495, 400)

        elements2 = driver.find_elements(By.XPATH,
                                         '//android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')

        for element in elements2:
            if element.text not in list_of_folder_names:
                list_of_folder_names.append(element.text)

        webcommon. close_driver()
        assert "test_folder" not in list_of_folder_names

    # Test 11
    def test_11_rename(self):
        # create folder
        os.system("adb shell mkdir /sdcard/test_folder")
        # rename folder
        os.system("adb shell mv /sdcard/test_folder /sdcard/secure_folder")

        webcommon = WebCommon("filemanager")
        webcommon.init_driver()
        driver = webcommon.get_driver()

        driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//android.view.ViewGroup[@index=0]')))
        except:
            print("timeout")
            driver.quit()

        driver.find_element(By.XPATH, "//android.widget.GridView/android.widget.LinearLayout[@index=0]").click()

        # wait for list items to appear
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                            'android.widget.ListView')))
        except:
            print("timeout")
            driver.quit()

        elements = driver.find_elements(By.XPATH,
                                        '//android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')

        list_of_folder_names = []
        for element in elements:
            list_of_folder_names.append(element.text)

        driver.swipe(500, 1670, 500, 495, 400)

        elements2 = driver.find_elements(By.XPATH,
                                         '//android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')

        for element in elements2:
            if element.text not in list_of_folder_names:
                list_of_folder_names.append(element.text)

        assert "secure_folder" in list_of_folder_names

        # delete folder
        os.system("adb shell rmdir /sdcard/secure_folder")

        webcommon.close_driver()

    # Test 12
    def test_12_exception(self):
        # create folder
        os.system("adb shell mkdir /sdcard/test_folder")

        # delete folder
        os.system("adb shell rmdir /sdcard/test_folder")

        webcommon = WebCommon("filemanager")
        webcommon.init_driver()
        driver = webcommon.get_driver()

        driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//android.view.ViewGroup[@index=0]')))
        except:
            print("timeout")
            driver.quit()

        driver.find_element(By.XPATH, "//android.widget.GridView/android.widget.LinearLayout[@index=0]").click()

        # wait for list items to appear
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                            'android.widget.ListView')))
        except:
            print("timeout")
            driver.quit()

        driver.swipe(500, 1670, 500, 495, 400)

        try:
            test_folder = driver.find_element(By.XPATH,
                                              '//android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[@text = "test_folder"]')
            test_folder.click()
        except:
            logger.info("Exception catched")
        finally:
            webcommon.close_driver()

    # Test 13
    def test_13_while(self):
        os.system("adb shell mkdir /sdcard/test_folder")

        webcommon = WebCommon("filemanager")
        webcommon.init_driver()
        driver = webcommon.get_driver()

        driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//android.view.ViewGroup[@index=0]')))
        except:
            print("timeout")
            driver.quit()

        driver.find_element(By.XPATH, "//android.widget.GridView/android.widget.LinearLayout[@index=0]").click()

        # wait for list items to appear with 10 sec timeout
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                            'android.widget.ListView')))
        except:
            print("timeout")
            driver.quit()

        elements = driver.find_elements(By.XPATH,
                                        '//android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')

        list_of_folder_names = []
        i = 0
        while i < len(elements):
            time.sleep(1)
            list_of_folder_names.append(elements[i].text)
            i += 1

        driver.swipe(500, 1670, 500, 495, 400)

        elements2 = driver.find_elements(By.XPATH,
                                         '//android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')
        j = 0
        while j < len(elements2):
            time.sleep(1)
            if elements2[j].text not in list_of_folder_names:
                list_of_folder_names.append(elements2[j].text)
            j += 1

        webcommon.close_driver()
        assert "test_folder" in list_of_folder_names
