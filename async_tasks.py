import time
import asyncio
async def one_process(i):
    '''
    當有 await 時已經是 coroutine
    而且 await 必須寫在 async def 裡面
    await 代表可以先跳過此程序, 它會自行偵測"asyncio.sleep(2)"結束後再執行下去, self replicating
    '''
    print(f' NO.{i} start ')
    await asyncio.sleep(2)
    print(f' NO {i} end')

if __name__ == "__main__":
    start_time = time.time()
    tasks = [one_process(i+1) for i in range(5)]

    # 如果tasks 裡面各項 function 擁有await 就必須使用 asyncio.wait
    # _async_create_tasks asyncio.gather 有順序, 此asyncio.run僅執行無順序
    asyncio.run(asyncio.wait(tasks))
    end_time = time.time()
    use_time = end_time-start_time
    print(f'use time: {use_time} s')

