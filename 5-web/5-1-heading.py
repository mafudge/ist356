from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.imdb.com/chart/top/")

    # Let's scrape the heading off the page!
    heading = page.query_selector("h1")

    # the tag name of the element
    tag =heading.evaluate("el => el.tagName")
    print(tag)

    # the contents of the element
    print(heading.inner_text())
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)