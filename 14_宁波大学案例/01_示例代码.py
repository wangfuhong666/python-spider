import re

import execjs
import requests


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

url = "https://uis.nbu.edu.cn/authserver/login"

params = {
    "service": "https://i.nbu.edu.cn/login#/apps"
}

user_name = "qwer"
password = "1234456"

# 创建一个会话，让第一次 GET 和后面的 POST 自动共用 Cookie
session = requests.Session()

# 第一次请求登录页，让服务器生成本次会话对应的：
# JSESSIONID、route、pwdEncryptSalt 和 execution
login_page = session.get(
    url,
    headers=headers,
    params=params
)
login_page.encoding = "utf-8"

# 页面上存在多个登录表单，也存在多个 execution，
# 所以必须先定位用户名密码登录表单 pwdFromId。
pwd_form_match = re.search(
    r'<form\b[^>]*\bid="pwdFromId"[^>]*>.*?</form>',
    login_page.text,
    re.S | re.I
)

if not pwd_form_match:
    raise RuntimeError("没有在登录页面中找到 pwdFromId 表单")

pwd_form_html = pwd_form_match.group(0)


def get_input_value(form_html, input_id):
    input_match = re.search(
        rf'<input\b[^>]*\bid="{re.escape(input_id)}"[^>]*>',
        form_html,
        re.I
    )

    if not input_match:
        raise RuntimeError(f"没有找到输入框：{input_id}")

    value_match = re.search(
        r'\bvalue="([^"]*)"',
        input_match.group(0),
        re.I
    )

    if not value_match:
        raise RuntimeError(f"输入框 {input_id} 没有 value 属性")

    return value_match.group(1)


# 从同一次 GET 返回的登录表单中提取动态参数
f1 = get_input_value(pwd_form_html, "pwdEncryptSalt")
execution = get_input_value(pwd_form_html, "execution")

with open("01.js", "r", encoding="utf-8") as f:
    js_code = f.read()

cry = execjs.compile(js_code)
pwd = cry.call("get_password", password, f1)

data = {
    "username": user_name,
    "password": pwd,
    "captcha": "",
    "_eventId": "submit",
    "cllt": "userNameLogin",
    "dllt": "generalLogin",
    "lt": "",
    "execution": execution
}

# 使用同一个 session 提交，不再手动传入 Cookie
response = session.post(
    url,
    headers=headers,
    params=params,
    data=data,
    allow_redirects=False
)

response.encoding = "utf-8"

print("状态码：", response.status_code)
print("跳转地址：", response.headers.get("Location"))
print(response.text)