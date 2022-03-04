from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def capabilities():
    desired_caps = {'platformName': 'Android',
                    'deviceName': 'Pixel_2_API_30',
                    'appPackage': 'io.cloudgrey.the_app',
                    'appActivity': 'io.cloudgrey.the_app.MainActivity'}
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver = capabilities()

def wait_and_return():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//android.view.ViewGroup[@index=0]')))
    except:
        print("timeout")
        driver.quit()

    list_elements = driver.find_elements(By.XPATH, '//android.view.ViewGroup[@index=0]')
    return list_elements

def test_07_wait():
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

    list_demo_element = driver.find_element(By.XPATH,
                                    '//android.view.ViewGroup[@index=1]/android.view.ViewGroup/android.widget.TextView[@text="List Demo"]')
    list_demo_element.click()

    list_of_elements = wait_and_return()

    elements_list = []

    i = 0
    while i < len(list_of_elements):
        elements_list.append(list_of_elements[i])
        i += 1

    assert len(elements_list) != 0