import asyncio
import time


def factorial2(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        time.sleep(1)
        f *= i
    return f

factorial2(3)
factorial2(4)


async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    return f


async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L)  # [2, 6, 24]


# asyncio.run(main())
