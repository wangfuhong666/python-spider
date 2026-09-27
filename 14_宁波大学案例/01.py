import requests
import execjs
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://uis.nbu.edu.cn",
    "Pragma": "no-cache",
    "Referer": "https://uis.nbu.edu.cn/authserver/login?service=https%3A%2F%2Fi.nbu.edu.cn%2Flogin%23%2Fapps",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "route": "0923bb5c51b66a6bcf4754511ebbcf01",
    "JSESSIONID": "2EAB7FC078AAEF1489A8F7BEC3F512EF",
    "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "zh_CN",
    "MULTIFACTOR_BROWSER_FINGERPRINT": "50F893BD810C5FB491E8B46631122291"
}
url = 'https://uis.nbu.edu.cn/authserver/login'
params = {
    "service": "https://i.nbu.edu.cn/login#/apps"
}

f1 ='gWSvcf5FefvlAApG'
user_name ='qwer'
password = '1234456'
with open('01.js', 'r',encoding='utf-8') as f:
    js_code = f.read()
    cry = execjs.compile(js_code)
    pwd =  cry.call('get_password',password,f1)
data = {
    "username": user_name,
    "password": pwd,
    "captcha": "",
    "_eventId": "submit",
    "cllt": "userNameLogin",
    "dllt": "generalLogin",
    "lt": "",
    "execution": "e1s1"
}

response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
response.encoding='utf-8'
print(response.status_code)
print(response)
print(response.text)
