import sys
from playwright.sync_api import sync_playwright

url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8787"
output = sys.argv[2] if len(sys.argv) > 2 else "screenshot.png"

with sync_playwright() as p:
    browser = p.chromium.launch(args=["--no-sandbox", "--disable-setuid-sandbox"])
    # Desktop view
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url, wait_until="networkidle")
    page.screenshot(path=output, full_page=True)
    browser.close()
    print("Screenshot saved to", output)
