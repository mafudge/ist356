from playwright.sync_api import Playwright, sync_playwright
import json 
from time import sleep

def course_scraper(playwright: Playwright, course) -> dict:
    # playwright codegen
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.goto("http://coursecatalog.syr.edu/")
    page.get_by_label("Search Keyword Field").click()
    page.get_by_label("Search Keyword Field, required").fill(course)
    page.get_by_label("Search Keyword Field, required").press("Enter")
    sleep(1)
    page.get_by_role("link", name=f"Best Match: {course}").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Print (opens a new window) ").click()
    
        page1 = page1_info.value
        page1.goto(page1.url)

        course_selector = page1.query_selector("table")
        course_text = course_selector.inner_text()

    # ---------------------
    context.close()
    browser.close()

    lines = course_text.split("\n")

    # figure out what is on each line....
    for i, line in enumerate(lines):
        print(i, line)

    return {
        "course": course,
        "title": lines[6].split("-")[-1].strip(),
        "credits": int(lines[8].split(" ")[0].strip()),
        "description": lines[9].strip()
    }

if __name__ == "__main__":
    courses = "IST 256, IST 387, IST 101, IST 356"
    course_data =  []
    with sync_playwright() as playwright:
        for course in courses.split(","):
            course_dict = course_scraper(playwright, course.strip())
            course_data.append(course_dict)
            print(course)
    with open("./5-web/cache/course_data.json", "w") as f:
        json.dump(course_data, f, indent=2)

