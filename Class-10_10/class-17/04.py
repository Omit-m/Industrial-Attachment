# To call async function (two ways)
# One way -> using asyncio.run()

import asyncio


# coroutine
async def hello():
    print("hello")


# coroutine
async def hi():
    print("hi")


asyncio.run(hello())
asyncio.run(hi())
asyncio.run(hello())
