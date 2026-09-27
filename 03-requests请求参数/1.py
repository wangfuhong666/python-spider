import requests
url="https://uploadfiles.nowcoder.com/images/20250701/0_1751342900843/D2B5CA33BD970F64A6301FA75AE2EB22"
head={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',

}
res=requests.get(url)
res.encoding="utf-8"
print(res.status_code)
print(res.request.headers)
#with open("牛客刷题统计1.png","wb") as f:
    #f.write(res.content)