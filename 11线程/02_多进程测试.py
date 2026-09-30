import multiprocessing
import os

def work(level):
    print(
        f"当前层数：{level}，"
        f"PID：{os.getpid()}，"
        f"父进程 PID：{os.getppid()}"
    )
    if level < 100000000000000:
        p = multiprocessing.Process(
            target=work,
            args=(level + 1,)
        )

        p.start()
        p.join()


if __name__ == '__main__':

    print(
        f"主进程 PID：{os.getpid()}"
    )

    p = multiprocessing.Process(
        target=work,
        args=(1,)
    )

    p.start()
    p.join()

    print("实验结束")
else:
    print(__name__)
