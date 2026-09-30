from DrissionPage._pages.chromium_page import ChromiumPage
import time
import requests
import os
page=ChromiumPage()
page.get("https://image.baidu.com/")
a = input("请输入你要爬取的图片内容")
b = int(input("请输入你要爬取的张数"))
page.ele("#chat-textarea").input(f"{a}")
page.ele("#ci-submit-button").click()
headers = {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "i",
    "referer": "https://image.baidu.com/",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}
for _ in range(11):
    #page.wait.load_end()
    time.sleep(1)
    page.run_js('window.scrollTo(0, 200)')
#div[@class="cos-masonry-container-item"]---->img-->src
di = page.eles('x:.//div[@class="cos-masonry-container-item"]')
print(len(di))
k=0
while os.path.exists(f"./{a}{k}"):
    k+=1
os.mkdir(f"./{a}{k}")
j = 0;
for i in di[0:b]:
    time.sleep(1)
    j+=1
    url = i.ele("x:.//img").attr("src")
    print(url)
    res = requests.get(url,headers=headers)
    print(res.status_code)
    with open(f"./{a}{k}/{a}{j}.jpg",'wb') as f:
        f.write(res.content)
