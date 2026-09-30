import requests
import time
"""

https://api.nba.cn/sib/v2/players/list?app_key=tiKB2tNdncnZFPOi&app_version=1.1.0&channel=NBA&device_id=3c9fc7ddec9b58823c1c96756dbd45d8&install_id=62886824&network=N%2FA&os_type=3&os_version=1.0.0&page_no=1&page_size=50&retireStat=A&sign=sign_v2&sign2=0DAEC3E8B483106197171E9C5A7BFF3E5A6DB7DD328012C6EFAD25B46DCD6F0B&t=1764682286

https://api.nba.cn/sib/v2/players/list?app_key=tiKB2tNdncnZFPOi&app_version=1.1.0&channel=NBA&device_id=3c9fc7ddec9b58823c1c96756dbd45d8&install_id=62886824&network=N%2FA&os_type=3&os_version=1.0.0&page_no=1&page_size=50&retireStat=A&sign=sign_v2&sign2=0DAEC3E8B483106197171E9C5A7BFF3E5A6DB7DD328012C6EFAD25B46DCD6F0B&t=1764682307

https://api.nba.cn/sib/v2/players/list?app_key=tiKB2tNdncnZFPOi&app_version=1.1.0&channel=NBA&device_id=e7c5fb07979c146db72fb0f664e3503d&install_id=62886824&network=N%2FA&os_type=3&os_version=1.0.0&page_no=3&page_size=50&retireStat=A&sign=sign_v2&sign2=D9E73D42803E55BDC32EC488A574475F2B2ED0FD353CB042C336FE2672A531E6&t=1764682328

"""
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}
a=int(input("请输入你要爬取的页数（1-11）"))
for j in range(1,a+1):
    now = round(time.time())
    url = f'https://api.nba.cn/sib/v2/players/list?app_key=tiKB2tNdncnZFPOi&app_version=1.1.0&channel=NBA&device_id=3c9fc7ddec9b58823c1c96756dbd45d8&install_id=62886824&network=N%2FA&os_type=3&os_version=1.0.0&page_no={j}&page_size=50&retireStat=A&sign=sign_v2&sign2=0DAEC3E8B483106197171E9C5A7BFF3E5A6DB7DD328012C6EFAD25B46DCD6F0B&t={now}'
    res = requests.get(url, headers=headers)
    for i in res.json()['data']:
        firstName = i['firstName']
        lastName = i['lastName']
        displayName = i['displayName']
        teamName = i['teamName']
        jerseyNo = i['jerseyNo']
        position = i['position']
        heightMetric = i['heightMetric']
        weightMetric = i['weightMetric']
        experience = str(i['experience'])
        country = i['country']
        with open(f"NBA{a}页数据.txt", "a+", encoding="utf-8") as f:
            f.write(' '.join([firstName, lastName, displayName, teamName, jerseyNo, position, heightMetric, weightMetric, experience, country]) + '\n\n')


