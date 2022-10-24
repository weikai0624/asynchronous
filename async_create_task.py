from re import I
import time
import asyncio
async def one_process(i):
    '''
    當有 await 時已經是 coroutine
    而且 await 必須寫在 async def 裡面
    await 代表可以先跳過此程序, 它會自行偵測"asyncio.sleep(2)"結束後再執行下去, self replicating
    '''
    print(f' NO.{i} start ')
    await asyncio.sleep(i)
    print(f' NO {i} end')

async def main():
    task1 = asyncio.create_task(one_process(1))
    task2 = asyncio.create_task(one_process(2))
    task3 = asyncio.create_task(one_process(3))
    await task1 
    await task2 
    await task3 


if __name__ == "__main__":
    start_time = time.time()
    
    asyncio.run(main())

    end_time = time.time()
    use_time = end_time-start_time
    print(f'use time: {use_time} s')

