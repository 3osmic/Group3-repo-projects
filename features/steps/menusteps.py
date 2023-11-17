import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image


@given('the user is on the restaurant\'s homepage')
def home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/")


@when('they click on the "Menu" section')
def open_menu(context):
    menu_button = context.driver.find_element(By.LINK_TEXT, 'MENU')
    menu_button.click()
    time.sleep(2)


@then('they should see a list of dishes and their prices')
def menu_list(context):
    menu_elements = context.driver.find_elements(By.CLASS_NAME, 'menu')
    assert len(menu_elements) > 0, "No 'menu' elements found on the page"
    time.sleep(2)
    screenshot = Image.open("screenshot-2.png")
    screenshot.show()


@then('close browser')
def close_browser(context):
    context.driver.close()
