import asyncio, random

async def set_async_timer(seconds, callback):
    await asyncio.sleep(seconds)
    await callback()

async def on_timer_end():
    print("Таймер сработал!")


async def main():
    await set_async_timer(2, on_timer_end)


if __name__ == "__main__":
    asyncio.run(main())
