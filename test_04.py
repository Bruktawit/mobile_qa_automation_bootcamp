from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def capabilities():
    desired_caps = {'platformName': 'Android',
                    'deviceName': 'Pixel_2_API_30',
                    'appPackage': 'io.cloudgrey.the_app',
                    'appActivity': 'io.cloudgrey.the_app.MainActivity'}
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def test_04_list_size():
    driver = capabilities()

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

    assert list_length == 7
