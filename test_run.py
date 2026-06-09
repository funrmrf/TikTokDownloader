import asyncio
from src.application.TikTokDownloader import TikTokDownloader
async def run():
    async with TikTokDownloader() as app:
        app._TikTokDownloader__update_menu()
        for item in app._TikTokDownloader__function_menu:
            print(item[0])

asyncio.run(run())
