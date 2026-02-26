from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        print("Navigating to Playwright Website...")
        page.goto("https://playwright.dev/")
        
        print("Taking a screenshot...")
        page.screenshot(path="playwright.png")
        print("Screenshot saved as playwright.png")

        title = page.title()
        print("Page title is:", title)
        browser.close()

if __name__ == "__main__":
    run()
