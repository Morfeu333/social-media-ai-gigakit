import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox", "--disable-setuid-sandbox"])
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        # Load local file
        await page.goto("file:///home/automatrix/Projects/social-media-ai-gigakit/public/index.html")
        await page.wait_for_timeout(1000)
        
        # Capture Top / Hero
        await page.screenshot(path="/home/automatrix/Projects/social-media-ai-gigakit/screenshot_v6_hero.png")
        
        # Scroll to NLE
        await page.evaluate("window.scrollTo(0, 1400)")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/automatrix/Projects/social-media-ai-gigakit/screenshot_v6_nle.png")
        
        # Scroll to Storyboard / HUD
        await page.evaluate("window.scrollTo(0, 2400)")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/automatrix/Projects/social-media-ai-gigakit/screenshot_v6_hud.png")

        # Scroll to Pricing
        await page.evaluate("window.scrollTo(0, 4800)")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/automatrix/Projects/social-media-ai-gigakit/screenshot_v6_pricing.png")
        
        await browser.close()
        print("Screenshots captured successfully!")

asyncio.run(main())
