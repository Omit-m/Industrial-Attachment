import asyncio
from datetime import datetime
import requests

async def get_post(post_id):
    response=requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code==200:
        print(response.json())
    else:
        print(" not found")


async def get_all_post():
    all_task=[]
    for id in range(1,40):
        task=asyncio.create_task(get_post(post_id = id))
        all_task.append(task)

        await asyncio.gather(*all_task)


print(datetime.now())
asyncio.run(get_all_post())
print(datetime.now())

