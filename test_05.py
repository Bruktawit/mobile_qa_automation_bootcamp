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


def get_element_by_text(text_input):
    elements = driver.find_elements(By.XPATH,
                                    '//android.view.ViewGroup[@index=1]/android.view.ViewGroup/android.widget.TextView')
    for element in elements:
        if element.text == text_input:
            return element


def test_05_text():
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

    list_demo_element = get_element_by_text("List Demo")
    list_demo_element.click()
