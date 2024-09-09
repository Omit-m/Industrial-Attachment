# Call asynchronously (2)

from datetime import datetime
import aiohttp
import asyncio

# beatuful soup , selenium,


async def get_post(post_id, session):
    response = await session.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )
    data = await response.text()
    print(data)
    await response.release()


async def get_all_post():

    # create the session
    session = aiohttp.ClientSession()

    all_task = []
    for id in range(1, 51):
        task = asyncio.create_task(get_post(post_id=id, session=session))
        all_task.append(task)

    await asyncio.gather(*all_task)

    await session.close()


print(datetime.now())
asyncio.run(get_all_post())
print(datetime.now())

# 2s
