from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
import os
import time
import re
t1 = time.time()
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=0, i",
    "referer": "https://music.163.com/",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "iframe",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}
cookies = {
    "JSESSIONID-WYYY": "KnWbnVRgc1rRJkZdscfq0xIgZFYK46BNvWXBYxnRG9ADzXg%2FIIfk9rMzeb5xq%2BT8eA78GvogJgTXwVzpyfky0Mh43z0IUUiDlW0%5CqDi2ID4yRmJH21upE%2BB%2FRTx%2FwHESVPt62lCXsOcftPXYkQkm6cuPxCTUR4y4eSI%2BC5671mHjh%2FuO%3A1787747715956",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "281e2e57d922f790e0406eac5d4e002b,1787745915999",
    "_ntes_nuid": "281e2e57d922f790e0406eac5d4e002b",
    "Hm_lvt_1483fb4774c02a30ffa6f0e2945e9b70": "1787745916",
    "HMACCOUNT": "96EBBD5BBDEC036A",
    "NMTID": "00OUF7_7N9l2MLHTkZhgdQWaUnbV2IAAAGgPfXXXw",
    "WEVNSM": "1.0.0",
    "WNMCID": "syzgau.1787745922880.01.0",
    "WM_NI": "0WvaGVSr1CxD33LWZIDL6I6bbJB9ZzeckBhXJojMFLOs%2BZT%2FSo1vlCOmz%2BLebioL2L46Wc63X8UW6SdpmALsSp2H%2BU%2F%2BR4b88fx5BqlUAqT2StrLekLzDhYdBtFKG68fTlc%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6ee97f345978c8587d074aa868fa7d55e869f8fade25a93eafd97e96182ef99a4e92af0fea7c3b92af489ba82c65e91aeffa4fb50f1ed84b8d9438894faaab56aa2968edad972a7bda5a3eb548ab1a6aec5488dade5bbd72591b1ff97ef498db3b6cccf6fa2b7a1adb148f8ea9984b5399ce89bb8b559a8b0a3a2cf7991b0fea9aa5fedf59ed5e134fcbab8d6c17bb08b8f92d73a91acbeade86190a68c89dc7082ac8aacc63efcba9c8de237e2a3",
    "WM_TID": "phXW7QXkAtxFVRQEFVfIVBqjujwU1TXj",
    "ntes_utid": "tid._.vgDZ2hRR%252BPlAFhVUVROdQU6z%252Bm0Nnuhq._.0",
    "sDeviceId": "YD-bbgW3yQp1lZFAkRRARLcBU6n7nhc2vlv",
    "Hm_lpvt_1483fb4774c02a30ffa6f0e2945e9b70": "1787746346"
}
'''
思路分析：⽹易云官⽅提供了免费歌曲的外链 http://music.163.com/song/media/oute r/url?id= ，
只需要把歌曲的 id 值拼接到这个链接最后，就是歌曲本体，所以需要去获取到 每⾸歌曲的歌曲名称与歌曲 id ，
id 在 href 值当中，所以取到 href 之后还需要做处理提 取出来 id 
'''
if not os.path.exists('案例'):
    os.makedirs('案例')
def get_content(name,url):
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    res = requests.get(url,headers=headers)
    with open(f'案例/{name}.mp3','wb') as f:
        f.write(res.content)

base_url ='http://music.163.com/song/media/outer/url?id='
#'div id="song-list-pre-cache"'
url = 'https://music.163.com/discover/toplist'
response = requests.get(url, headers=headers, cookies=cookies)
tree =etree.HTML(response.text)
li_list = tree.xpath('.//div[@id="song-list-pre-cache"]/ul/li')
with ThreadPoolExecutor(max_workers=100) as executor:
    for li in li_list:
        id = li.xpath('./a/@href')[0].split("=")[1]
        name = li.xpath('./a/text()')[0]
        print(base_url+id,name)
        executor.submit(get_content,name,base_url+id)

t2 = time.time()

print(t2-t1)