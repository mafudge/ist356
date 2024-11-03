from playwright.sync_api import Playwright, sync_playwright, expect
import requests

def download_image(url): 
    filename = url.split("/")[-1]
    response = requests.get(url) 
    with open(filename, 'wb') as file: 
        file.write(response.content)
    return filename

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    site = "https://ist256.com/fall2023/"
    page.goto(site)

    image = page.query_selector("img.logo")
    image_source = image.get_attribute("src")
    print(image_source)

    filename = download_image(site + image_source)
    print(filename)
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)