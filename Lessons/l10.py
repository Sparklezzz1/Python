import asyncio, random
#couritine(Коурутина)
#task(задача)
#event loop(цикл событий)
#future(promise)

# async def f(x):
#     await asyncio.sleep(1)
#     print(x)
#     if (x == 3):
#         await f("HERE!")

# async def main():
#     a = f(1)
#     b = f(2)
#     c = f(3)
#     d = f(4)
#     g = f(5)
#     h = f(6)
#     print("asdsad")
#     await c
#     await d

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        await asyncio.sleep(time_to_sleep)
        print("{} waited {} seconds".format(name, time_to_sleep))


async def main():
    await asyncio.wait([waiter("first"), waiter("second"), waiter("third"), waiter("fourth")])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())