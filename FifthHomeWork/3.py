import asyncio
import aiohttp

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses

async def main():
    urls = ["https://github.com", "https://google.com"]
    
    results = await fetch_multiple_urls(urls)
    for response in results:
        print(response.status)

if __name__ == "__main__":
    asyncio.run(main())
    