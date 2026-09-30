import requests

# 1.明确目标
url = 'https://my.4399.com/'
# 2.发起请求，接受响应
head={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',

    'Referer':'https://www.4399.com/flash/zmhj.htm?g=4'
}
res = requests.get(url)
res.encoding='utf-8'
print(res.text)
# 3.数据解析（提取）


# 4.数据存储