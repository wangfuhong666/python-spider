import execjs
import requests
import time
import jsonpath
import json
import os
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.kugou.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "kg_mid": "b36c019bf55de6e1353531a57041fe50",
    "kg_dfid": "4FL90z1KtMfa1Dmkch2Tny2Z",
    "kg_dfid_collect": "d41d8cd98f00b204e9800998ecf8427e",
    "KuGoo": "KugooID=1385700841&KugooPwd=60133FF6F66104419734311C7FAEDC7E&NickName=%u9648%u6668&Pic=http://imge.kugou.com/kugouicon/165/20100101/20100101192931478054.jpg&RegState=1&RegFrom=&t=8d46830ab7049809057e891ab9e760eecdcefa66d05e13f2c5a9bcaef7dbb78f&a_id=1014&ct=1788183778&UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0031%u0033%u0038%u0035%u0037%u0030%u0030%u0038%u0034%u0031&t1=",
    "KugooID": "1385700841",
    "t": "8d46830ab7049809057e891ab9e760eecdcefa66d05e13f2c5a9bcaef7dbb78f",
    "a_id": "1014",
    "UserName": "kgopen1385700841",
    "mid": "b36c019bf55de6e1353531a57041fe50",
    "dfid": "4FL90z1KtMfa1Dmkch2Tny2Z",
    "Hm_lvt_aedee6983d4cfc62f509129360d6bb3d": "1788001102,1788075585,1788154488,1788236773",
    "HMACCOUNT": "96EBBD5BBDEC036A",
    "kg_mid_temp": "b36c019bf55de6e1353531a57041fe50",
    "Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d": "1788237349"
}
url = 'https://complexsearch.kugou.com/v2/search/song'
params = {
    "callback": "callback123",
    "srcappid": "2919",
    "clientver": "1000",
    "clienttime": f"{int(time.time() * 1000)}",
    "mid": "b36c019bf55de6e1353531a57041fe50",
    "uuid": "b36c019bf55de6e1353531a57041fe50",
    "dfid": "4FL90z1KtMfa1Dmkch2Tny2Z",
    "keyword": "邓紫棋",
    "page": "1",
    "pagesize": "30",
    "bitrate": "0",
    "isfuzzy": "0",
    "inputtype": "0",
    "platform": "WebFilter",
    "userid": "1385700841",
    "iscorrection": "1",
    "privilege_filter": "0",
    "filter": "10",
    "token": "8d46830ab7049809057e891ab9e760eecdcefa66d05e13f2c5a9bcaef7dbb78f",
    "appid": "1014",
    "signature": "209ad77330ef50b620bf85d0f075c63f"
}
'''
"NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014bitrate=0"
"callback=callback123"
"clienttime=1788024635540"
"clientver=1000"
"dfid=4FL90z1KtMfa1Dmkch2Tny2Z"
"filter=10"
"inputtype=0"
"iscorrection=1"
"isfuzzy=0"
"keyword=周杰伦"
"mid=b36c019bf55de6e1353531a57041f"
"page=1"
"pagesize=30"
"platform=WebFilter"
"privilege_filter=0"
"srcappid=2919token=user"
"id=0uuid=b36c019bf55de6e1353531a57041fe50NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"'''
data = (
    f"NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
    f"appid={params['appid']}"
    f"bitrate={params['bitrate']}"
    f"callback={params['callback']}"
    f"clienttime={params['clienttime']}"
    f"clientver={params['clientver']}"
    f"dfid={params['dfid']}"
    f"filter={params['filter']}"
    f"inputtype={params['inputtype']}"
    f"iscorrection={params['iscorrection']}"
    f"isfuzzy={params['isfuzzy']}"
    f"keyword={params['keyword']}"
    f"mid={params['mid']}"
    f"page={params['page']}"
    f"pagesize={params['pagesize']}"
    f"platform={params['platform']}"
    f"privilege_filter={params['privilege_filter']}"
    f"srcappid={params['srcappid']}"
    f"token={params['token']}"
    f"userid={params['userid']}"
    f"uuid={params['uuid']}"
    f"NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
)
with open('01.js', "r", encoding='utf-8') as f:
    js_code = f.read()
    cry = execjs.compile(js_code)
    params['signature'] = cry.call('get_signature', data)
response = requests.get(url, headers=headers, params=params,cookies=cookies)
print(response)
print(response.status_code)
res  =response.text
res = res[res.find('{'):res.rfind('}') + 1]
res = json.loads(res)
if not os.path.exists("邓紫棋"):
    os.makedirs('邓紫棋')
print(res)
for song_id in jsonpath.jsonpath(res, '$..EMixSongID'):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Origin": "https://www.kugou.com",
        "Pragma": "no-cache",
        "Referer": "https://www.kugou.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = 'https://wwwapi.kugou.com/play/songinfo'
    params = {
        "srcappid": "2919",
        "clientver": "20000",
        "clienttime": f"{int(time.time() * 1000)}",
        "mid": "b36c019bf55de6e1353531a57041fe50",
        "uuid": "b36c019bf55de6e1353531a57041fe50",
        "dfid": "4FL90z1KtMfa1Dmkch2Tny2Z",
        "appid": "1014",
        "platid": "4",
        "encode_album_audio_id": song_id,
        "token": "8d46830ab7049809057e891ab9e760eecdcefa66d05e13f2c5a9bcaef7dbb78f",
        "userid": "1385700841",
        "signature": "3b43d7f07b4acbbc9d87294f6a186077"
    }
    data = (
        f"NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
        f"appid={params['appid']}"
        f"clienttime={params['clienttime']}"
        f"clientver={params['clientver']}"
        f"dfid={params['dfid']}"
        f"encode_album_audio_id={params['encode_album_audio_id']}"
        f"mid={params['mid']}"
        f"platid={params['platid']}"
        f"srcappid={params['srcappid']}"
        f"token={params['token']}"
        f"userid={params['userid']}"
        f"uuid={params['uuid']}"
        f"NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
    )
    with open('01.js', "r", encoding='utf-8') as f:
        js_code = f.read()
        cry = execjs.compile(js_code)
        params['signature'] = cry.call('get_signature', data)
    response = requests.get(url, headers=headers, params=params)
    print(response.json())
    res = response.json()
    mp3_url = jsonpath.jsonpath(res, '$..play_url')[0]
    song_name = jsonpath.jsonpath(res, '$..audio_name')[0]
    print(song_name, mp3_url)
    res = requests.get(mp3_url, headers=headers)
    with open(f'邓紫棋/{song_name}.mp3', 'wb') as f:
        f.write(res.content)


