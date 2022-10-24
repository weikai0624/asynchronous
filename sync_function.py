import time
from tracemalloc import start 

def one_process(i):
    print(f' NO.{i} start ')
    time.sleep(2)
    print(f' NO {i} end')

if __name__ == "__main__":
    start_time = time.time()
    for i in range(5):
        one_process(i+1)
    end_time = time.time()
    use_time = end_time-start_time
    print(f'use time: {use_time} s')

