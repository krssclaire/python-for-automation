import numpy as np
from playwright.sync_api import sync_playwright

moves = 100

# prepare playwright
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=100)
page = browser.new_page()
page.goto('https://play2048.co/')

print(f'Playing: making {moves} moves')

# limited times of slides
for t in range(moves):      
    # randomize move
    randomized = np.random.randint(0, 4)

    # assign value to key
    if randomized == 0:
        page.keyboard.press('ArrowUp')
    elif randomized == 1:
        page.keyboard.press('ArrowRight')
    elif randomized == 2:
        page.keyboard.press('ArrowDown')
    else:
        page.keyboard.press('ArrowLeft') 
    
    # progession status
    print(f'Move n° {t}/{moves}') 

browser.close()
playwright.stop()

print('Done')