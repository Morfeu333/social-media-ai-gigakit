import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox", "--disable-setuid-sandbox"])
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("file:///home/automatrix/Projects/social-media-ai-gigakit/public/index.html")
        await page.wait_for_timeout(1000)
        
        # Capture Hero Showcase full view
        await page.evaluate("window.scrollTo(0, 520)")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/automatrix/Projects/social-media-ai-gigakit/screenshot_v6_showcase.png")
        
        # Capture Marquee + NLE
        await page.evaluate("window.scrollTo(0, 1150)")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/automatrix/Projects/social-media-ai-gigakit/screenshot_v6_marquee_nle.png")
        
        await browser.close()
        print("Captured scrolled views")

asyncio.run(main())
