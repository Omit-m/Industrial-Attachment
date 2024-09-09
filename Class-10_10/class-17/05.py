import asyncio


# coroutine
async def hello():
    print("hello")


# coroutine
async def hi():
    print("hi")


# await hello() ---> not possible


# we need an async function to call (await) another async function
async def main():
    await hello()
    await hi()
    await hello()


asyncio.run(main())
