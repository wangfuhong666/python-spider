from lxml import etree
import csv
import requests
from loguru import logger
logger.add(
    #生成文件路径
    sink='logs/hupu{time:YYYY-MM-DD HH-mm-ss}.log',
    #
    rotation="00:00",
    retention="7 days",#
    encoding="utf-8",#日志编码方式
    level='INFO',#当前模块的日志级别
    format='{time:YYYY-MM-DD HH:mm:ss} {level} {message}'#日志格式

)
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Google Chrome\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}


def get_detail(url):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    tree = etree.HTML(response.text)
    data_list = tree.xpath('(//div[@class="thread-content-detail"])[1]//text()')
    img_list = tree.xpath('//div[@class="slate-image"]//img/@data-origin')
    data_detail = ''.join(data_list) if data_list else ''
    img = '\n'.join(img_list) if img_list else ''
    # print(data)
    a = f"{data_detail}\n{img}"
    # print(img)
    return a

sum = [
    ["标题", "回复量", "浏览量", "作者", "时间", "详情页数据"]
]
url = "https://bbs.hupu.com/stock-1"
response = requests.get(url, headers=headers)
print(response.status_code)
tree = etree.HTML(response.text)
data = tree.xpath('//div[@class="bbs-sl-web-post"]//li[@class="bbs-sl-web-post-body"]')
print(len(data))
for li in data:
    # 标题
    a1 = li.xpath('.//div[@class="post-title"]/a/text()')[0]
    a2 = li.xpath('.//div[@class="post-datum"]/text()')[0]  # string
    # 回复/浏览
    a21 = a2.split('/')[0].strip()  # 回复量
    a22 = a2.split('/')[1].strip()  # 浏览量
    # print(a21,a22)
    # 作者
    a3 = li.xpath('.//div[@class="post-auth"]/a/text()')[0]
    # print(a3)
    # 时间
    a4 = li.xpath('.//div[@class="post-time"]/text()')[0]
    # print(a4)
    # 详情页链接  https://bbs.hupu.com
    a5 = li.xpath('.//div[@class="post-title"]/a/@href')[0]
    a6 = 'https://bbs.hupu.com' + a5
    # print(a6)
    info = get_detail(a6)
    logger.info(f"{a1} {a2} {a3} {a4} {a5} {info}")
    sum.append([a1, a21, a22, a3, a4, info])
with open("多页采集实战001.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sum)
# print(response.text)
# print(response)
