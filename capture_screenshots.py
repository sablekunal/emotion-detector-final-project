import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Test 1: Application Deployment
        await page.goto('http://localhost:5000/emotion?text=I am happy today')
        await page.screenshot(path='6b_deployment_test.png')
        
        # Test 2: Error Handling Interface
        await page.goto('http://localhost:5000/emotion?text=')
        await page.screenshot(path='7c_error_handling_interface.png')
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
