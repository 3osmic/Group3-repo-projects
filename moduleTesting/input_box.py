from fixtures._fixtures import timeout
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # opens a new page
    page = context.new_page()

    # go to Cuisine Home Page
    page.goto("https://cbarnc.github.io/Group3-repo-projects/")

    page.locator('id=comments').click(timeout=5000)

    input_data = 'I love this restaurant'
    page.locator('id=comments').fill(input_data)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

