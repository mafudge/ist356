from playwright.sync_api import Playwright, sync_playwright, expect

url = "https://coursecatalog.syracuse.edu/undergraduate/information-studies/applied-data-analytics-bs/"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    content = page.content()
    print(content)
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)