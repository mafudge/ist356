from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023/syllabus/")

    # Let's scrape the heading off the page!
    headings = page.query_selector_all("h2, h3")
    for heading in headings:
        tag = heading.evaluate('el => el.tagName').lower()
        text = heading.inner_text()
        if tag == "h2":
            print(text)
        else:
            print(f"\t{text}")    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)