import requests

# 1.明确目标
url = 'http://8.137.170.29:3000/api/leaderboard'

# 2.发起请求，接受响应
respond = requests.get(url)
print(respond)
#print(respond.request.headers)
respond.encoding = 'utf-8'
print(respond.text)
# 3.数据解析（提取）


# 4.数据存储
with open('小鱼.txt', 'w',encoding='utf-8') as f:
    f.write(respond.text)