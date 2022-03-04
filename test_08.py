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


def scroll_method(start_x, start_y, end_x, end_y, duration):
    driver.swipe(start_x, start_y, end_x, end_y, duration)


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

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//android.view.ViewGroup[@index=0]')))
    except:
        print("timeout")
        driver.quit()

    scroll_method(150, 1700, 150, 500, 800)

    last_item = driver.find_element(By.XPATH,
                                    '//android.view.ViewGroup[@index=1]/android.view.ViewGroup[@index=14]/android.widget.TextView')
    last_item_text = last_item.text

    assert last_item_text == "Stratus"
