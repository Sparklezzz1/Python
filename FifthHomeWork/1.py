import asyncio

async def fetch_url(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = [
        "1",
        "2",
        "3",
        "4",
        "5"
    ]
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())