import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        page.on("console", lambda msg: print(f"Browser console: {msg.text}"))
        
        print("Running Test 1")
        await page.goto('http://127.0.0.1:5000/')
        await page.fill('#textToAnalyze', 'I am so happy I am doing this.')
        await page.click('button')
        try:
            await page.wait_for_function("document.getElementById('system_response').innerText.length > 0", timeout=5000)
        except Exception as e:
            print("Error waiting for response 1:", e)
            print(await page.content())
        await page.screenshot(path='6b_deployment_test.png')
        
        print("Running Test 2")
        await page.goto('http://127.0.0.1:5000/')
        await page.fill('#textToAnalyze', '')
        await page.click('button')
        try:
            await page.wait_for_function("document.getElementById('system_response').innerText === 'Invalid text! Please try again!'", timeout=5000)
        except Exception as e:
            print("Error waiting for response 2:", e)
            print(await page.content())
        await page.screenshot(path='7c_error_handling_interface.png')
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
