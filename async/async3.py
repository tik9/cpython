import asyncio
import time

async def hello(i):
    print(f"hello {i} started")
    await asyncio.sleep(1)
    # time.sleep(1)
    print(f"hello {i} done")


async def main():
    # returns immediately, the task is created
    task1 = asyncio.create_task(hello(1))
    # await asyncio.sleep(2)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

asyncio.run(main())
