import requests
url = 'https://www.baidu.com/'
response = requests.get(url)
print(response.encoding)
response.encoding = 'utf-8'
print(response.apparent_encoding)
with open('test.html', 'w',encoding='utf-8') as f:
    f.write(response.text)