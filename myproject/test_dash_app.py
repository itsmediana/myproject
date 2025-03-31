import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto("http://localhost:8050")

        # Проверяем, что заголовок на странице присутствует
        assert "График пользователей" in await page.text_content("h1")

        # Проверяем, что график отобразился
        graph = await page.query_selector("#user-age-graph")
        assert graph is not None

        print("✅ Автотест пройден успешно!")

        await browser.close()

asyncio.run(main())
