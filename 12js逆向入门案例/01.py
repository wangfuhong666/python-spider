import execjs
import requests

headers = {
    "sec-ch-ua-platform": "\"Windows\"",
    "Referer": "https://mp.weixin.qq.com/",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua-mobile": "?0"
}
use_name = '123'
password = '123456'
with open('01.js', "r", encoding='utf-8') as f:
    js_code = f.read()
    cry = execjs.compile(js_code)
    pwd = cry.call('get_pwd', password)
url = 'https://mp.weixin.qq.com/cgi-bin/bizlogin'
params = {
    "action": "startlogin"
}
data = f'username={123}&pwd={pwd}&verify_ticket=&rand_str=&f=json&userlang=zh_CN&redirect_url=&fingerprint=e2f4b71f7927d5cdd0db11891d416daa&token=&lang=zh_CN&ajax=1'.encode(
    'utf-8', 'surrogateescape')
response = requests.post(url,headers=headers,params=params, data=data)
print(response)
print(response.status_code)
print(response.text)

