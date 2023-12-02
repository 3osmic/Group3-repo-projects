_______________________________________________________________________

	Group 3	Playwright Testing LAB	
_______________________________________________________________________


## LAB 05	Browser Automation With Playwright

### OBJECTIVES
- Understand the importance of browser automation.
- Automate website functionalities using Python's Playwright library
- Create pytest functions
- Provide details on commands


### PREREQUISITES
- Must have basic knowledge of software testing
- Must have a basic level of knowledge of the python programming language
- Must have a basic level of knowledge of html
- Must have knowledge about how to use locators
- Must have basic knowledge of javascript

## BEFORE YOU GET STARTED
You will need the following in order for your tests to perform correctly

- Install a web browser to run the web application
    - This can be:
        - Firefox (Recommended)
        - Chrome
        - Microsoft Edge
- Create a GitHub account
  - Clone the GitHub repository
- Install a code editor
- Install playwright
- Install pytest
- Install pytest-playwright

Examples of code editors:
- VS Code
- Pycharm (Recommended)

### OVERVIEW
This lab serves as a dedicated environment for developers and testers to experiment with and refine automation scripts using the Playwright framework. It provides a controlled space for testing browser interactions, debugging code, and optimizing scripts for web application automation. The information below is a step-by-step guide on how to help you get started.

For more information on GitHub: https://github.com/CbarNC/Group3-repo-projects/blob/Selenium/Selenium%20Lab.md


### What Is Playwright?
Playwright is an open-source browser automation library that allows developers to automate interactions with web pages.

For more information on playwright, navigate to this website: https://playwright.dev

### Step 1: Install Playwright
To install playwright, type the following command in either your command line or terminal:

`pip install playwright`



https://github.com/CbarNC/Group3-repo-projects/assets/137305186/6fa7ddc6-0302-4a9e-abfe-f56a9e599551



### Step 2: Install Pytest
To install pytest, type the following command in either your command line or terminal:

`pip install pytest`



https://github.com/CbarNC/Group3-repo-projects/assets/137305186/3e8c6ac6-52f6-4101-b04b-a28899568cb2



### Step 3: Install Pytest-Playwright
To install pytest-playwright, type the following command in either your command line or terminal:

`pip install pytest-playwright`




https://github.com/CbarNC/Group3-repo-projects/assets/137305186/9da6f4ac-efde-4be0-a786-bc71c6b365b4



### Step 4: Install New Browsers
In order for you to install new browsers, you need to enter the following command into the command line or terminal:

`playwright install`

This command installs the latest versions of the three browsers that Playwright supports: Chromium, Firefox, and WebKit.



https://github.com/CbarNC/Group3-repo-projects/assets/137305186/776fa3e5-7d7c-44ac-93e2-a6644ad2c582



### Step 5: Testing the Webpage
Below is a breakdown example of the following code in order for you to be able to test your webpage.

```python
from playwright.sync_api import Playwright, sync_playwright


def test_webpage(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # opens a new page
    page = context.new_page()

    # starting from the Cuisine Home Page
    page.goto("https://cbarnc.github.io/Group3-repo-projects/")

    # travel to the about page
    page.get_by_role("link", name="about").click()

    page.wait_for_timeout(2000)

    page.screenshot(path="screenshotAbout.png")

    page.wait_for_timeout(2000)

    # travel to the menu page
    page.get_by_role("link", name="menu").click()

    page.screenshot(path="screenshotMenu.png")

    # page.wait_for_timeout(2000)

    # # travel to the signin page
    page.get_by_text('SIGN IN').click()

    page.screenshot(path='screenshotSignin.png')

    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_webpage(playwright)

```



https://github.com/CbarNC/Group3-repo-projects/assets/137305186/3c0aa2c1-6c58-4ff7-9c59-67dbb5ae368e



### Step 6: Testing the Input Box (Contact Us)
Below is a breakdown example of the following code in order for you to be able to test your input box.

```python
from playwright.sync_api import Playwright, sync_playwright


def test_input_box(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # opens a new page
    page = context.new_page()

    # go to Cuisine Home Page
    page.goto("https://cbarnc.github.io/Group3-repo-projects/")

    page.locator('id=comments').click(timeout=5000)

    comment_text = 'I love this restaurant'
    page.locator('id=comments').fill(comment_text)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_input_box(playwright)


```



https://github.com/CbarNC/Group3-repo-projects/assets/137305186/50a80837-7fd2-4683-9173-e9ff443fd58a



### Step 7: Testing the Radio Button (Contact Us)
Below is a breakdown example of the following code in order for your you to be able to test your radio button.

```python
from playwright.sync_api import Playwright, sync_playwright


def test_radio_button(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # opens a new page
    page = context.new_page()

    # go to Cuisine Home Page
    page.goto("https://cbarnc.github.io/Group3-repo-projects/")

    page.locator('#yes').click()

    page.screenshot(path="screenshotYes.png")

    page.wait_for_timeout(2000)

    # now change radio button selection from yes to no

    page.locator('#no').click(timeout=5000)

    page.wait_for_timeout(2000)

    # save screenshot of no radio button being selected

    page.screenshot(path="screenshotNo.png")

    page.wait_for_timeout(500)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_radio_button(playwright)

```



https://github.com/CbarNC/Group3-repo-projects/assets/137305186/00b1837f-b475-4b1d-a9ee-2bbfed2f36a8



## FAQ (Frequently Asked Questions)
 <a id="faq"></a>
