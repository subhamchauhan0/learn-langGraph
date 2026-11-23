import asyncio


async def function():
    print("this is function1")
    await asyncio.sleep(2)
    print("function end")


async def function1():
    print("this is function 2")
    await asyncio.sleep(2)
    print("function 2 end")


async def main():
    await asyncio.gather(function(), function1())


asyncio.run(main())