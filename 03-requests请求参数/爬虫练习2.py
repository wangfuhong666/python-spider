import requests

# 1.明确目标
url = 'https://www.baidu.com/'
# 2.发起请求，接受响应
head = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'cookie':'PSTM=1772769940; BAIDUID=7C837624ABCFA479A37BC19B018F31CC:FG=1; PAD_BROWSER=1; BIDUPSID=C825D95545567253598CB2AC3159ED57; BD_UPN=12314753; BAIDUID_BFESS=7C837624ABCFA479A37BC19B018F31CC:FG=1; ZFY=Jyty:B:Axw5akGq:Ad3dsSkBqs0WSrXGonEom3I:AAd2wIM:C; H_PS_PSSID=67862_67885_67889_67945_67913_67951_67954_67956_67974_68053_68074_68085_68089_67985_68003_68126_68128_68142_68147_68151_68150_68140_68165_68182_68190_68232_68242_68262_68258_68267_68281_68284_68292; BD_HOME=1; BA_HECTOR=8k842405010k8h212g808501008l8g1kr7uju26',
    'host': 'www.baidu.com'
}
respond = requests.get(url, headers=head)
print(respond)
respond.encoding = 'utf-8'
print(respond.request.headers)
print(respond.status_code)
print(respond.text)
# 3.数据解析（提取）


# 4.数据存储
