from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from io import StringIO

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://mafudge.github.io/scraping-examples/ist256/fall2023/")

    # Let's scrape the page!
    # use pandas read_html to parse the HTML

    # get a list of all tables on the page
    content = StringIO(page.content())
    dfs = pd.read_html(content)

    # print the first table
    print(dfs[0])
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
