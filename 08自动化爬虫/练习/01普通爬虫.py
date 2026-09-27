import time
import requests
import csv
from lxml import etree

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}
url = 'https://stats.ioinformatics.org/results/2025'
head = ["contestant","member","score_abs","score_rel","award"]
sum = []
res = requests.get(url, headers=headers)
tree = etree.HTML(res.text)
tr = tree.xpath('//div[@class="maincontent"]/table/tr')
i = 0
for li in tr:
    if(i>=2):
        time.sleep(1)
        contestant = li.xpath("./td[2]/a/text()")[0]
        member =  " "if li.xpath("./td[3]/a/text()") == [] else li.xpath("./td[3]/a/text()")[0]
        score_abs = li.xpath("./td[10]/text()")[0]
        SCORE_rel = li.xpath("./td[11]/text()")[0]
        award = "not award"if li.xpath("./td[12]/text()") == [] else li.xpath("./td[12]/text()")[0]
        sum.append([contestant,member,score_abs,SCORE_rel,award])
    i+=1
#div[@class="maincontent"]-> table border='1'->第三个tr标签下
with open('01/IOI2025.csv','w',encoding='utf-8-sig',newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(head)
    csvwriter.writerows(sum)
'''
                    <tr>
                        <td class="gold">1</td>
                        <td class="gold leftalign">
                            <a href="people/8606">Hengxi Liu</a>
                        </td>
                        <td class="gold leftalign">
                            <a href="members/CHN">China</a>
                        </td>
                        <td class="gold taskscore">100</td>
                        <td class="gold taskscore">100.00</td>
                        <td class="gold taskscore">100</td>
                        <td class="gold taskscore">100</td>
                        <td class="gold taskscore">91.23</td>
                        <td class="gold taskscore">100</td>
                        10
                        <td class="gold">591.23</td>
                        11
                        <td class="gold">98.54%</td>
                        12
                        <td class="gold">Gold</td>
                    </tr>
'''

#print(response.text)
#print(response)