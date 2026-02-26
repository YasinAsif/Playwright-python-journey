from playwright.sync_api import sync_playwright

def practice_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")
        print("Page title is:", page.title())
        browser.close()

if __name__ == "__main__":
    practice_test()
