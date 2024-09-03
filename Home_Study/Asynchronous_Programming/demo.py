import asyncio
from datetime import datetime
async def num_01(a,b):
    print(" num_1")
    sum = a + b
    print(sum)

    print("num_1 finished")
    await asyncio.sleep(5)


async def num_2(a, b):
    print(" num_2")
    minus = a - b
    print(minus)

    print("num_2 finished")
    await asyncio.sleep(1)

async def num_3(a, b):
   print (" num_3")
   multipley = a * b
   print(multipley)

   print ("num_3 finished")
   await asyncio.sleep(5)


async def main():
    print(datetime.now())
    await num_01(10, 5)
    await num_2(10, 5)
    await num_3(10, 5)
    print(datetime.now())

asyncio.run(main())
