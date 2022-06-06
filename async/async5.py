import asyncio
import time
import random


async def eat():
    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    # time.sleep(wait)

    print("Done Eating")


async def sleep():
    wait = random.randint(0, 1)
    # time.sleep(wait)
    await asyncio.sleep(wait)
    print("Done Sleeping")


async def main():
    for x in range(2):
        await asyncio.gather(eat(), sleep())
        time.sleep(1)
        print("+", "-"*20)

if __name__ == "__main__":
    # t = time.perf_counter()
    asyncio.run(main())
    t = time.process_time()
    t2 = time.perf_counter()

    print(f'Total time elapsed: {t2:.2f}, {t} seconds')
