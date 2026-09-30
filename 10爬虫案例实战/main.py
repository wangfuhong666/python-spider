import csv
import requests
from lxml import etree
import re

def get_con(text, html):
    con = re.findall(
        text,
        html,
        re.S
    )
    if not con:
        return ''

    value = con[0].replace('&nbsp;', ' ').replace('&emsp;', ' ')
    return re.sub(r'\s+', ' ', value).strip()


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
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

url = 'https://c.gongkong.com/'
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
tr = etree.HTML(response.text)
li_list = tr.xpath('.//div[@class="main_bot_l_text"]/ul/li')

# j = 0
head =['公司名称','详情页url','邮箱','网址','电话','地址','邮编/联系人','传真']
sum=[]
for li in li_list:
    data=[]
    con = li.xpath('./a/text()')[0]
    url = 'https:' + li.xpath('./a/@href')[0]
    print(con, url)
    data.extend([con,url])
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'

    '''
    if 'y_Contact' in res.text:
        name = re.findall(
            r'名称[:：].*?<a.*?>(.*?)</a>',
            res.text,
            re.S
        )
        if not name:
            print(url)
            with open('error.txt', 'w', encoding='utf-8') as f:
                f.write(res.text)
    
    '''

    # j += 1
    # if j == 10:
    #     break

    if 'y_Contact' in res.text:
        # 名称
        name = get_con(
            r'名称[:：].*?<a.*?>(.*?)</a>',
            res.text
        )

        # 地址
        place = get_con(
            r'地址：(.*?)</p>',
            res.text
        )

        # 邮编
        sta = get_con(
            r'邮编：(.*?)</p>',
            res.text
        )

        # 电话
        phone = get_con(
            r'电话：(.*?)</p>',
            res.text
        )

        # 传真
        zhi = get_con(
            r'传真：(.*?)(?:</p|<p)',
            res.text
        )

        # 网址
        c_url = get_con(
            r'>网址：<a.*?>(.*?)</a></p>',
            res.text
        )

        # Email
        email = get_con(
            r'Email：<a.*?>(.*?)</a></p>',
            res.text
        )
        data.extend([email,c_url,phone,place,sta,zhi])
        print(name, place, sta, phone, zhi, c_url, email)
    else:
        # 联系人
        name = get_con(
            r'<h1 id="Rtitle_D">(.*?)</h1>',
            res.text
        )

        # 邮箱
        email = get_con(
            r'<b>邮&emsp;箱</b>：(.*?)</p>',
            res.text
        )

        # 网址
        c_url = get_con(
            r'<b>网&emsp;址</b>：(.*?)</p>',
            res.text
        )

        # 电话
        phone = get_con(
            r'<b>电&emsp;话</b>：(.*?)</p>',
            res.text
        )

        # 地址
        place = get_con(
            r'<b>地&emsp;址</b>：(.*?)</p>',
            res.text
        )
        data.extend([email,c_url,phone,place,name,''])
        print(name, place, phone, c_url, email)
    sum.append(data)
with open('中国工控网.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(head)
    writer.writerows(sum)