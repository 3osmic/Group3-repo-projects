from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image


@given('the user is on the login page')
def login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/signIn.html")


@when('they enter valid username and password')
def user_pass(context):
    ui = "test_user123"
    pi = "password123"
    context.driver.find_element(By.ID, 'login-username').send_keys(ui)
    time.sleep(2)
    context.driver.find_element(By.ID, 'login-password').send_keys(pi)
    time.sleep(2)
    screenshot = Image.open("screenshot-2.png")
    screenshot.show()


@when('click the "Login" button')
def click_login(context):
    login_button = context.driver.find_element(By.ID, 'login-submit')
    login_button.click()
    time.sleep(5)


@then('they should be redirected to the dashboard')
def redirect(context):
    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/")
