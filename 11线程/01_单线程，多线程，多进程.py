import requests
import time
import threading
import os
import multiprocessing


url_list = [
    (
        '怎么唱情歌',
        'http://music.163.com/song/media/outer/url?id=255219'
    ),
    (
        '跳楼机',
        'http://music.163.com/song/media/outer/url?id=2645500113'
    ),
    (
        '罗生门',
        'http://music.163.com/song/media/outer/url?id=1456890009'
    ),
]


# =========================
# 多线程使用的函数
# =========================
def get_content_thread(name, url):
    with open(f'music2/{name}.mp3', 'wb') as f:
        content = requests.get(url).content
        f.write(content)


# =========================
# 多进程使用的函数
# =========================
def get_content_process(name, url):
    with open(f'music3/{name}.mp3', 'wb') as f:
        content = requests.get(url).content
        f.write(content)


# =========================
# 主程序
# =========================
if __name__ == '__main__':

    # =========================
    # 1. 单线程爬取
    # =========================

    if not os.path.exists('music1'):
        os.mkdir('music1')

    t1 = time.time()

    for name, url in url_list:
        with open(f'music1/{name}.mp3', 'wb') as f:
            content = requests.get(url).content
            f.write(content)

    t2 = time.time()

    print('单线程爬取时间：', t2 - t1)


    # =========================
    # 2. 多线程爬取
    # =========================

    if not os.path.exists('music2'):
        os.mkdir('music2')

    thread_list = []

    t3 = time.time()

    for name, url in url_list:

        t = threading.Thread(
            target=get_content_thread,
            args=(name, url)
        )

        t.start()

        thread_list.append(t)


    for t in thread_list:
        t.join()


    t4 = time.time()

    print('多线程爬取时间：', t4 - t3)


    # =========================
    # 3. 多进程爬取
    # =========================

    if not os.path.exists('music3'):
        os.mkdir('music3')

    process_list = []

    t5 = time.time()

    for name, url in url_list:

        p = multiprocessing.Process(
            target=get_content_process,
            args=(name, url)
        )

        p.start()

        process_list.append(p)


    for p in process_list:
        p.join()


    t6 = time.time()

    print('多进程爬取时间：', t6 - t5)