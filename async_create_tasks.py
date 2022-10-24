from re import I
import time
import asyncio
async def one_process(num):
    print('第 {} 任務，第一步'.format(num))
    await asyncio.sleep(2)
    print('第 {} 任務，第二步'.format(num))
    return '第 {} 任務完成'.format(num)

async def raise_error(num):
    raise ValueError
    print('這邊不會執行到')

async def main():
    # _async_create_tasks asyncio.gather 可以指定順序
    tasks = [ one_process(i) for i in range(5)]
    tasks1 = [raise_error(i) for i in range(5)]
    # results = await asyncio.gather(*tasks, return_exceptions=True)
    results = await asyncio.gather(*tasks, *tasks1, return_exceptions=True)
    print(results)

if __name__ == "__main__":
    start_time = time.time()
    
    #此asyncio.run僅執行無順序
    asyncio.run(main())

    end_time = time.time()
    use_time = end_time-start_time
    print(f'use time: {use_time} s')

