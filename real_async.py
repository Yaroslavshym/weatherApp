import asyncio
import time



async def foo():
    print('One')
    await asyncio.sleep(1)
    # time.sleep(1)
    print('Two')


async def main():
    await asyncio.gather(foo(), foo(), foo(),)


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(__file__, end - start)