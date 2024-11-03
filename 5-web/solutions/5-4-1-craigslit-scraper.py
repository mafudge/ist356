from playwright.sync_api import Playwright, sync_playwright
from time import sleep
import json 

def scrape_craigslist(playwright: Playwright, search:str) -> list[dict]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"https://syracuse.craigslist.org/search/sss?query={search}#search=1~gallery~0~0")
    sleep(2)
    page.locator(".cl-search-view-mode > span").click()
    page.get_by_role("button", name=" list").click()

    scraped_items = []
    results = page.query_selector("div.results")
    items = results.query_selector_all("li")
    for item in items:
        if item is None:
            continue
        title = item.get_attribute("title")
        price_selector = item.query_selector("span.priceinfo") 
        price = price_selector.inner_text() if price_selector else "N/A"
        link_selector = item.query_selector("a")
        link = link_selector.get_attribute("href") if link_selector else "N/A"
        text =item.inner_text().split("\n\n")[-1]
        others  = text.split("·")
        location = others[1].strip()

        scraped_items.append({
            "title": title,
            "price": price,
            "location": location,
            "link": link
        })
    
    # ---------------------
    context.close()
    browser.close()

    return scraped_items


if __name__ == "__main__":
    search = input()        
    with sync_playwright() as playwright:
        items = scrape_craigslist(playwright, search)
        print(json.dumps(items))
