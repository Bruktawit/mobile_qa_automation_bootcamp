from appium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

def capabilities():
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "Pixel_2_API_30",
        "automationName": "UiAutomator2",
        "appPackage": "com.alphainventor.filemanager",
        "appActivity": "com.alphainventor.filemanager.activity.MainActivity"
    }
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)


def test_13_while():
    os.system("adb shell mkdir /sdcard/test_folder")
    driver = capabilities()

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

    assert "test_folder" in list_of_folder_names
