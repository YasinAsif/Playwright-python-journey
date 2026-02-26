from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        # Login is required for SauceDemo
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        
        # Click Login button using get_by_role
        page.get_by_role("button", name="Login").click()
        
        # Verify successful login
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        
        # Interact with inventory
        page.get_by_role("button", name="Add to cart").first.click()
        
        print("Test passed: Logged in and added item to cart.")
        
        browser.close()

if __name__ == "__main__":
    run()

