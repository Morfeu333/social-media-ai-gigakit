import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox", "--disable-setuid-sandbox"])
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("file:///home/automatrix/Projects/social-media-ai-gigakit/public/index.html")
        await page.wait_for_timeout(1000)

        # 1. Click on the main CTA button to trigger Quiz Modal
        print("Clicking hero CTA button...")
        await page.click(".btn-cta")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/automatrix/Projects/social-media-ai-gigakit/screenshot_modal_step1.png")
        print("Modal Step 1 captured.")

        # 2. Answer Question 1
        await page.click("#m-quiz-step-1 .quiz-opt-btn:first-child")
        await page.wait_for_timeout(300)
        
        # 3. Answer Question 2
        await page.click("#m-quiz-step-2 .quiz-opt-btn:first-child")
        await page.wait_for_timeout(300)

        # 4. Answer Question 3
        await page.click("#m-quiz-step-3 .quiz-opt-btn:first-child")
        await page.wait_for_timeout(500)

        # 5. Capture the Modal showing the 3 offers revealed below
        await page.screenshot(path="/home/automatrix/Projects/social-media-ai-gigakit/screenshot_modal_completed_offers.png")
        print("Modal Completed Offers captured!")

        await browser.close()

asyncio.run(main())
