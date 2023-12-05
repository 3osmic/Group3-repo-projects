from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image


@given('the user is on the registration page')
def user_on_registration(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://cbarnc.github.io/Group3-repo-projects/signup.html')
    time.sleep(5)


@when('the user fills in their information')
def user_fills_information(context):
    context.driver.find_element(By.NAME, "username").send_keys("test_user123")
    time.sleep(2)
    context.driver.find_element(By.ID, "signUpEmail").send_keys("johndoe@example.com")
    time.sleep(2)
    context.driver.find_element(By.NAME, "password").send_keys("password123")
    time.sleep(2)
    context.driver.find_element(By.NAME, "confirm-password").send_keys("password123")
    time.sleep(2)
    screenshot = Image.open("BrowserScreenshots/screenshot1.png")
    screenshot.show()


@when('clicks the "Register" button')
def click_register(context):
    submit_confirm = context.driver.find_element(By.ID, "signupSubmit")
    submit_confirm.click()
    time.sleep(5)


@then('the user should be logged in')
def redirect(context):
    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/")
