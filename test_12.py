from appium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def capabilities():
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "Pixel_2_API_30",
        "automationName": "UiAutomator2",
        "appPackage": "com.alphainventor.filemanager",
        "appActivity": "com.alphainventor.filemanager.activity.MainActivity"
    }
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

def test_12_exception():
    #create folder
    os.system("adb shell mkdir /sdcard/test_folder")

    #delete folder
    os.system("adb shell rmdir /sdcard/test_folder")

    driver = capabilities()

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

