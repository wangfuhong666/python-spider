import requests
import execjs
import time
import json
import jsonpath
import csv
with open( 'encrypt.js','r',encoding='utf-8') as f:
    js_code = f.read()
    cry = execjs.compile(js_code)
url = "https://www.zq12369.com/api/newzhenqiapi.php"

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.zq12369.com",
    "Pragma": "no-cache",
    "Referer": "https://www.zq12369.com/environment.php?order=desc&tab=rank",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

data = {
    "param": cry.call('get_param',int(time.time() * 1000))
}

response = requests.post(url,headers=headers,data=data)

print(response.status_code)
print(response.text)
with open( 'decrypt.js','r',encoding='utf-8') as f:
    js_code = f.read()
    cry = execjs.compile(js_code)
res = cry.call('decrypt_response', response.text)
data = json.loads(res)
print(data)
rows = data["result"]["data"]["rows"]
#print(rows)
head = ['时间', '城市名称', '城市ID', '省份', 'AQI', '空气质量', '首要污染物']

with open("城市空气质量排名表.csv", "w", encoding="utf-8-sig", newline="") as f:
    csvwriter = csv.writer(f)

    csvwriter.writerow(head)

    for item in rows:
        csvwriter.writerow([
            item["time"],
            item["cityname"],
            item["cityid"],
            item["provincename"],
            item["aqi"],
            item["quality"],
            item["primary_pollutant"]
        ])