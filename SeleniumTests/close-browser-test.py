from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://cbarnc.github.io/Group3-repo-projects/") # Gets the website

# Maximizing window
driver.maximize_window()

# Time before window closes
time.sleep(2)

# Close Edge browser
driver.quit()