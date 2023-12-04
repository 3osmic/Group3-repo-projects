from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://cbarnc.github.io/Group3-repo-projects/") # Gets the website

# Get the url of the new tab
driver.execute_script("window.open('https://cbarnc.github.io/Group3-repo-projects/about.html', '_blank');")

# Switch to a new tab
driver.switch_to.window(driver.window_handles[1])

# Time before tab closes
time.sleep(5)

# Close tab
driver.close()

# Switch back to original url
driver.switch_to.window(driver.window_handles[0])


# Time before browser closes
time.sleep(2)


# Close Edge browser
driver.quit()