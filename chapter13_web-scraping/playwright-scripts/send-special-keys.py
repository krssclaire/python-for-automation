from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=750)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
page.locator('html').press('End')  # Scrolls to bottom
page.locator('html').press('Home')  # Scrolls to top
browser.close()
playwright.stop()