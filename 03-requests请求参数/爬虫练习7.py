"""
https://www.douban.com/group/search?cat=1019&q=%E8%A5%BF%E6%B8%B8%E8%AE%B0
https://www.douban.com/group/search?cat=1019&q=%E5%93%88%E5%93%88%E5%93%88
https://www.douban.com/group/search?start=20&cat=1019&sort=time&q=%E5%93%88%E5%93%88%E5%93%88
https://www.douban.com/group/search?start=40&cat=1019&sort=time&q=%E5%93%88%E5%93%88%E5%93%88
https://www.douban.com/group/search?start=60&cat=1019&sort=time&q=%E5%93%88%E5%93%88%E5%93%88
https://www.douban.com/group/search?start=80&cat=1019&sort=time&q=%E5%93%88%E5%93%88%E5%93%88
https://www.douban.com/group/search?start=10*当前页数&cat=1019&sort=time&q=名称
"""
import requests
import os

name = input("请输入你要获取的内容")
num = int(input("请输入你要获取的页数"))
if not os.path.exists(name):
    os.mkdir(name)

num += 1
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
    'cookie': 'bid=RbnHPQdUavc; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1764501073%2C%22https%3A%2F%2Fwww.doubao.com%2F%22%5D; _pk_id.100001.8cb4=136b428290019142.1764501073.; _pk_ses.100001.8cb4=1; ap_v=0,6.0; __utma=30149280.1029414048.1764501074.1764501074.1764501074.1; __utmc=30149280; __utmz=30149280.1764501074.1.1.utmcsr=doubao.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __yadk_uid=9T1gGkAHO17Se98h980d2njZVmEvJTRq; ct=y; __utmb=30149280.10.10.1764501074',

}

for i in range(1, num):
    url = f"https://www.douban.com/group/search?start={10 * i}&cat=1019&sort=time&q={name}"
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    with open(f'./{name}/{name}{i}.html', 'w', encoding='utf-8') as f:
        f.write(res.text)






