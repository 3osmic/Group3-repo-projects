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
