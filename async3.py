import asyncio
import time


def hello(i):
    print(f"hello {i} start")
    time.sleep(2)
    print(f"hello {i} end")

# hello(1)
# time.sleep(1)
# hello(2)


async def hello(i):
    print(f"hello {i} started")
    await asyncio.sleep(2)
    print(f"hello {i} done")


async def main():
    # returns immediately, the task is created
    task1 = asyncio.create_task(hello(1))
    await asyncio.sleep(2)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

asyncio.run(main())
