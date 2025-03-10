import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.flipkart.com/")
    page.wait_for_url("https://www.flipkart.com/")
    page.get_by_label("Mobiles").click()
    expect(page.get_by_role("link", name="iPhone 16", exact=True)).to_be_
    page.get_by_role("link", name="iPhone 16", exact=True).first.click()
    page.get_by_role("button", name="Buy Now").click()
    print('code executed successfully')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
