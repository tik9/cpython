from asynchat import async_chat
import asyncio
import time


def main():
    async_task()


async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)


async def sleep2():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)


async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep2()
        total += number
    print(f'Task {name}: Sum = {total}\n')


# def async_task():
start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')


if __name__ == 'main':
    main()
