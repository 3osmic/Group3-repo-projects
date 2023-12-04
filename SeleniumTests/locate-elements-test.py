from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://cbarnc.github.io/Group3-repo-projects/") # Gets the website

# Maximizing window
driver.maximize_window()

# Find element by tag name
h2 = driver.find_element(By.TAG_NAME, "h2")
print(h2.text)

h3 = driver.find_element(By.TAG_NAME, "h3")
print(h3.text)

p = driver.find_element(By.TAG_NAME, "p")
print(p.text)