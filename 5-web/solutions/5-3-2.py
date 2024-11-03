from playwright.sync_api import Playwright, sync_playwright
import json 
from time import sleep

def stock_scraper(playwright: Playwright, stock, date) -> dict:
    # playwright codegen
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"https://finance.yahoo.com/quote/{stock}/")
    sleep(1)

    price = page.query_selector("fin-streamer.livePrice").get_attribute("data-value")
    
    # ---------------------
    context.close()
    browser.close()

    # return dict
    return {
        "symbol": stock,
        "date": date,
        "price": price
    }


if __name__ == "__main__":
    from datetime import datetime

    portfolio = [ "AAPL" , "AMZN" , "GM", "HD", "META", "NET" ]
    date = datetime.today().strftime('%Y-%m-%d')
    portfolio_data = []
    with sync_playwright() as playwright:
        for stock in portfolio:
            stock_dict = stock_scraper(playwright, stock, date)
            portfolio_data.append(stock_dict)
            print(stock_dict)

    with open(f"./5-web/cache/{date}-portfolio_data.json", "w") as f:
        json.dump(portfolio_data, f, indent=2)