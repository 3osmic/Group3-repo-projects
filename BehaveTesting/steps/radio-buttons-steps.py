from Screenshot import Screenshot
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image


@given('user on contact us section')
def contact_us(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://cbarnc.github.io/Group3-repo-projects/')


@when('the selects the Yes Radio button')
def select_button(context):
    radio_list = context.driver.find_elements(By.NAME, "T3C_member")
    for radioButton in radio_list:
        radioButton_t = radioButton.get_attribute("value")
        if radioButton_t == "yes":
            radioButton.click()
            time.sleep(4)


@then('the user should see radio button yes selected')
def radio_status(context):
    ob = Screenshot.Screenshot()
    img_url = ob.full_screenshot(context.driver, save_path=r'.', image_name='myRadioimage.png', is_load_at_runtime=True,
                                 load_wait_time=0)
    screenshot = Image.open(img_url)
    screenshot.show()
