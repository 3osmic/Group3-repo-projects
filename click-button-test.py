from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://cbarnc.github.io/Group3-repo-projects/") # Gets the website

# Maximizing window
driver.maximize_window()

# Click a button
driver.find_element(By.XPATH, "/html/body/div/aside/section[2]/form/fieldset/button").click()