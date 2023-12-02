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
