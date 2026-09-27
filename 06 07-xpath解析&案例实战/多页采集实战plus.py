import csv
import time
import requests
from lxml import etree


headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def get_detail(url):
    response = requests.get(url, headers=headers, timeout=20)
    print("详情页状态码：", response.status_code)

    # 每请求一条详情页，等待 2 秒
    time.sleep(2)

    # 出现 405 等异常就返回 None
    if response.status_code != 200:
        print("详情页被拒绝，本次停止采集。")
        return None

    tree = etree.HTML(response.text)

    data_list = tree.xpath(
        '(//div[@class="thread-content-detail"])[1]//text()'
    )
    img_list = tree.xpath(
        '//div[@class="slate-image"]//img/@data-origin'
    )

    data_detail = "".join(data_list)
    img = "\n".join(img_list)

    return f"{data_detail}\n{img}"


result = [
    ["标题", "回复量", "浏览量", "作者", "时间", "详情页数据"]
]

stop = False

# x 依次是 1、2、3、4、5
for x in range(1, 11):
    # 拼接出：https://bbs.hupu.com/stock-1、stock-2……stock-5
    url = f"https://bbs.hupu.com/stock-{x}"

    response = requests.get(url, headers=headers, timeout=20)
    print(f"\n第 {x} 页状态码：", response.status_code)

    tree = etree.HTML(response.text)
    data = tree.xpath(
        '//div[@class="bbs-sl-web-post"]'
        '//li[@class="bbs-sl-web-post-body"]'
    )
    print(f"第 {x} 页帖子数量：", len(data))

    for li in data:
        # 标题
        a1 = li.xpath('.//div[@class="post-title"]/a/text()')[0]

        # 回复量、浏览量
        a2 = li.xpath('.//div[@class="post-datum"]/text()')[0]
        a21 = a2.split("/")[0].strip()
        a22 = a2.split("/")[1].strip()

        # 作者
        a3 = li.xpath('.//div[@class="post-auth"]/a/text()')[0]

        # 时间
        a4 = li.xpath('.//div[@class="post-time"]/text()')[0]

        # 详情页链接
        a5 = li.xpath('.//div[@class="post-title"]/a/@href')[0]
        a6 = "https://bbs.hupu.com" + a5

        # 详情页数据
        info = get_detail(a6)

        # 如果详情页出现 405，结束所有分页循环
        if info is None:
            stop = True
            break

        result.append([a1, a21, a22, a3, a4, info])

    if stop:
        break

    # 爬完一页后也等 2 秒，再进入下一页
    time.sleep(2)

with open("多页采集实战05.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(result)

print("采集结束，共保存：", len(result) - 1, "条数据")