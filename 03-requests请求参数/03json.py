import requests
import time
url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1783920836130&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=1&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Referer": (
        "https://careers.tencent.com/search.html?"
        "query=ot_40001001,ot_40001002,ot_40001003,"
        "ot_40001004,ot_40001005,ot_40001006,at_1"
    ),
    "Sec-CH-UA": (
        '"Not;A=Brand";v="8", '
        '"Chromium";v="150", '
        '"Google Chrome";v="150"'
    ),
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}
for j in range(1,11):
    params = {
        "timestamp": f"{time.time()}",
        "countryId": "",
        "cityId": "",
        "bgIds": "",
        "productId": "",
        "categoryId": "40001001,40001002,40001003,40001004,40001005,40001006",
        "parentCategoryId": "",
        "attrId": "1",
        "keyword": "",
        "pageIndex": f"{j}",
        "pageSize": "10",
        "language": "zh-cn",
        "area": "cn",
    }
    res = requests.get(url=url, headers=headers, params=params)
    # print(res.json()['Data']['Posts'][0])
    content = res.json()['Data']['Posts']
    i = 1;
    with open("腾讯招聘信息", "a", encoding='utf-8') as f:
        for item in content:
            tem = ""
            tem += f"{i}\n----------------------\n"
            for key, value in item.items():
                tem += f"{key}: {value}\n"
            tem += "\n\n\n\n"
            f.write(tem)
            i += 1
        f.write("####################################################\n\n")