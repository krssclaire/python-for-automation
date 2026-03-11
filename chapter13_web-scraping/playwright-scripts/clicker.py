from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
page.click('input[type=checkbox]')  # Checks the checkbox
page.click('input[type=checkbox]')  # Unchecks the checkbox
page.click('a')  # Clicks the link
page.go_back()
checkbox_elem = page.get_by_role('checkbox')  # Calls a Locator method
checkbox_elem.check()  # Checks the checkbox
checkbox_elem.uncheck()  # Unchecks the checkbox
checkbox_elem.set_checked(True)  # Checks the checkbox
checkbox_elem.set_checked(False)  # Unchecks the checkbox
page.get_by_text('is a link').click()  # Uses a Locator method
browser.close()
playwright.stop()