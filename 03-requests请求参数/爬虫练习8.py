import requests
import time
from urllib.parse import quote
import os
"""
https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1764584789134&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=1&pageSize=10&language=zh-cn&area=cn'

https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1764586297415&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=2&pageSize=10&language=zh-cn&area=cn

https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1764586355582&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=3&pageSize=10&language=zh-cn&area=cn


"""
#1.明确目标
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'

}
name=input('请输入你要了解的岗位')
num=int(input('请输入你要爬取的页数'))

for j in range(1,num+1):
    now=round(time.time())
    encoded_name = quote(name, encoding='utf-8')
    #print     f
    url = f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={now}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={encoded_name}&pageIndex={j}&pageSize=10&language=zh-cn&area=cn'
    # 2.发起请求，接收响应
    res = requests.get(url, headers=headers)
    # print(res.json())
    # 3.数据解析
    list1 = res.json()['Data']['Posts']
    for i in list1:
        RecruitPostName = i['RecruitPostName']
        LocationName = i['LocationName']
        LastUpdateTime = i['LastUpdateTime']
        Responsibility = i['Responsibility'].replace('\n','')
        # 4.存储数据
        #print(RecruitPostName,LocationName,LastUpdateTime,Responsibility,'\n')
        with open(f'腾讯招聘{name}的{num}页内容.txt', 'a', encoding='utf-8') as f:
            f.write('\n'.join([RecruitPostName, LocationName, LastUpdateTime, Responsibility])+'\n\n\n')













