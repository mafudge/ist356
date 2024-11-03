from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.imdb.com/chart/top/")

    # outer element that contains the list of 250 top movies
    top_250_list = page.query_selector("ul.ipc-metadata-list")

    # same selector from there
    elements_on_page = top_250_list.query_selector_all("h3.ipc-title__text")
    for element in elements_on_page:
        title = element.inner_text()
        print(title)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)