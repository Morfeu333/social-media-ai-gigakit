import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Launch browser with real Chrome headers to bypass Cloudflare 1010
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-blink-features=AutomationControlled"
            ]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()
        print("Navigating to GHL...")
        await page.goto("https://app.gohighlevel.com/", wait_until="networkidle")
        print("Current URL:", page.url)
        print("Title:", await page.title())
        await page.screenshot(path="/home/automatrix/Projects/social-media-ai-gigakit/ghl_login_screen.png")
        print("Screenshot saved to ghl_login_screen.png")
        await browser.close()

asyncio.run(main())
