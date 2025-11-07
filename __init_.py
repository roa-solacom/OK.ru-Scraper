#import requests
#cookies_string= 'JSESSIONID:"b17a49da21d7c9711d6cb3a128bc4969f66aad94ed8d9be2.f96875a6"; 

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # You can set headless=False to see the browser
    page = browser.new_page()
    
    # Navigate to Ok.ru login page
    page.goto("https://ok.ru")

    # Login (SELETORS CAN BE ADJUSTED)
    page.fill('input[name="Mobile phone or e-mail address"]', '08094350233')
    page.fill('input[name="Password"]', 'l0dah0gatu')
    page.press('input[name="Password"]', 'Log in to OK')

    # Wait for login to complete and the feed to load
    page.wait_for_selector('div.feed-item')

    # Scrape the content (for example, posts from the feed)
    content = page.content()

    # Parse with BeautifulSoup
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    posts = soup.find_all('div', {'class': 'feed-item'})
    
    for post in posts:
        print(post.text)

    browser.close()
