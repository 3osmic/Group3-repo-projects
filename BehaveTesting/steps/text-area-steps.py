import time
from Screenshot import *
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image


@given('The comments box is empty')
def empty_comments(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://cbarnc.github.io/Group3-repo-projects/')
    assert context.driver.find_element(By.ID, 'comments').text == ''
    # takes a screenshot of the empty text area before user writes
    ob = Screenshot.Screenshot()
    img_url = ob.full_screenshot(context.driver, save_path=r'.', image_name='myimage2.png', is_load_at_runtime=True,
                                 load_wait_time=0)
    screenshot = Image.open(img_url)
    screenshot.show()


@when(u'The user selects the input box and types a message')
def test_message(context):
    sendMessage = "This is a Test Message"
    context.driver.find_element(By.ID, 'comments').send_keys(sendMessage)
    time.sleep(3)
    ob = Screenshot.Screenshot()
    img_url2 = ob.full_screenshot(context.driver, save_path=r'.', image_name='myimage.png', is_load_at_runtime=True,
                                  load_wait_time=0)
    print(img_url2)


# takes a screenshot of message user wrote
@then(u'The comment box is filled')
def message_status(context):
    screenshot = Image.open("myimage.png")
    screenshot.show()
