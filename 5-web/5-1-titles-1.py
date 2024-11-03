from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.imdb.com/chart/top/")
    
    # select the title by selector
    elements_on_page = page.query_selector_all("h3.ipc-title__text")
    for element in elements_on_page:
        title = element.inner_text()
        print(title)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)