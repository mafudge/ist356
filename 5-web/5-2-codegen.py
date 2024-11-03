import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    course = "IST 356"

    # playwright codegen
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.goto("http://coursecatalog.syr.edu/")
    page.get_by_label("Search Keyword Field").click()
    page.get_by_label("Search Keyword Field, required").fill(course)
    page.get_by_label("Search Keyword Field, required").press("Enter")
    page.get_by_role("link", name=f"Best Match: {course}").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Print (opens a new window) ").click()
    
        page1 = page1_info.value
        page1.goto(page1.url)

        course_selector = page1.query_selector("table")
        course_text = course_selector.inner_text()
        print(course_text)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
