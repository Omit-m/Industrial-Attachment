import asyncio
from datetime import datetime


# coroutine
async def hello():
    print("hello called")
    await asyncio.sleep(5)
    print("hello finished")


# coroutine
async def hi():
    print("hi called")
    await asyncio.sleep(1)
    print("hi finished")


# await hello() ---> not possible


# we need an async function to call (await) another async function
async def main():
    task = []

    task.append(asyncio.create_task(hello()))
    task.append(asyncio.create_task(hi()))
    task.append(asyncio.create_task(hello()))

    await asyncio.gather(*task)



asyncio.run(main())
