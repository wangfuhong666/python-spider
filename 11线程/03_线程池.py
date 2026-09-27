from concurrent.futures import ThreadPoolExecutor
import time
from tkinter.font import names


def task(n):

    print(f"task{n} is start")
    time.sleep(1)
    print(f"task{n} is end")

with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(10):
        executor.submit(task,i)

