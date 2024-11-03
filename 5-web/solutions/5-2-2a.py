from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from time import sleep
import sys

def run(playwright: Playwright, year) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"https://cuse.com/sports/football/schedule/{year}")
    page.wait_for_load_state("load")
    sleep(1)
    page.get_by_role("tab", name="Table View not selected").click()
    sleep(1)
    dfs = pd.read_html(page.content())
    
    
    # ---------------------
    context.close()
    browser.close()
    return dfs[0].to_html(index=False)


with sync_playwright() as playwright:
    year = input()
    html_table = run(playwright, year = str(year))
    print (html_table)
