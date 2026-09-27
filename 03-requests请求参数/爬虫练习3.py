import requests

# 1.明确目标
url='https://img1.baidu.com/it/u=534307473,2869005599&fm=253&fmt=auto&app=138&f=JPEG?w=875&h=500'

# 2.发起请求，接受响应
res = requests.get(url)
# 3.数据解析（提取）


# 4.数据存储
with open('宇宙.jpg','wb') as f1:
    f1.write(res.content)
