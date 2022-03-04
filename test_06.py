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

def test_06_send_keys():
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

    echo_box_item = driver.find_element(By.XPATH,
                                    '//android.view.ViewGroup[@index=1]/android.view.ViewGroup/android.widget.TextView[@text="Echo Box"]')
    echo_box_item.click()

    try:
        element = WebDriverWait(driver, 10).until(
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
    assert saved_text == "Hello world"

