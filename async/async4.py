import asyncio
import time


async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        # time.sleep(1)
        await asyncio.sleep(1)
        f *= i
    return f


async def main():
    fac = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(fac)  # [2, 6, 24]


asyncio.run(main())
