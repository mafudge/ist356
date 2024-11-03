from playwright.sync_api import Playwright, sync_playwright
from time import sleep

def run(playwright: Playwright, url) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    sleep(2) # wait for page 
    
    # get body content as text
    content = page.query_selector("body").text_content() 

    # ---------------------
    context.close()
    browser.close()

    return content


with sync_playwright() as playwright:
    # input from other program
    url = input()
    
    text = run(playwright, url)

    # output to other program
    print(text)