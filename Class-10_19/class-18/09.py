
import asyncio

async def my_task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)  # Simulate a delay (e.g., I/O operation)
    print(f"Task {name} completed after {delay} seconds")


async def main():
    # Create tasks
    task1 = asyncio.create_task(my_task("A", 2))
    task2 = asyncio.create_task(my_task("B", 5))
    task3 = asyncio.create_task(my_task("C", 3))
    # Optionally, you can wait for the tasks to complete
    await task1
    await task2
    await task3


# Run the main function
asyncio.run(main())
