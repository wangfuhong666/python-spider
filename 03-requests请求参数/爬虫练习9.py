import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'

}
url = 'https://careers.tencent.com/tencentcareer/api/post/Query'
params = {
    'timestamp': '1764586355582',
    'countryId': '',
    'cityId': '',
    'bgIds': '',
    'productId': '',
    'categoryId': '',
    'parentCategoryId': '',
    'attrId': '',
    'keyword': 'python',
    'pageIndex': '3',
    'pageSize': '10',
    'language': 'zh-cn',
    'area': 'cn'
}
res = requests.get(url, headers=headers, params=params)

# 2.发起请求，接收响应

# print(res.json())
# 3.数据解析
list1 = res.json()['Data']['Posts']
for i in list1:
    RecruitPostName = i['RecruitPostName']
    LocationName = i['LocationName']
    LastUpdateTime = i['LastUpdateTime']
    Responsibility = i['Responsibility'].replace('\n', '')
    print(RecruitPostName, LocationName, LastUpdateTime, Responsibility)
