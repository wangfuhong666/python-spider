import execjs
import requests
import re
from lxml import etree
session = requests.Session()
with open('get_pwd.js', "r",encoding='utf-8') as f:
    js_code = f.read()
    cry = execjs.compile(js_code)
user_name = '1q2w3e4r'
password = '123456'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Referer": "http://shanzhi.spbeen.com/login/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
}
#字体加密
font_map = {
    '龒': '0',
    '麣': '1',
    '餼': '2',
    '閏': '3',
    '龤': '4',
    '鑶': '5',
    '驋': '6',
    '齤': '7',
    '龥': '8',
    '鸺': '9',
}
font_map = str.maketrans(font_map)
session.headers.update(headers)

url = 'http://shanzhi.spbeen.com/login/'
response = session.get(url,verify=False)
response.encoding='utf-8'
print(response.text)
print(response)
tree = etree.HTML(response.text)
pk = tree.xpath('.//input[@id="pk"]/@value')[0]
csrfmiddlewaretoken = tree.xpath('.//input[@name="csrfmiddlewaretoken"]/@value')[0]
print(pk)
print(csrfmiddlewaretoken)
pwd =cry.call('get_password',password,pk)
url = 'http://shanzhi.spbeen.com/login/'

data = {
    'username': user_name,
    'password': pwd,
    'csrfmiddlewaretoken': csrfmiddlewaretoken
}

response = session.post(url,data=data,verify=False)
base_url = 'http://shanzhi.spbeen.com'
print(response.status_code)
print(response.text)
print(response)
tree = etree.HTML(response.text)
for add_url in tree.xpath('.//div[@class="card-body"]/a/@href'):
    url  = base_url + add_url
    #print(url)
    response = session.get(url,verify=False)
    # print(response.status_code)
    # print(response.text)
    tree = etree.HTML(response.text)
    name = tree.xpath('.//div[@class="jumbotron bg-white"]/h4/text()')[0]
    name = re.findall('.*：(.*)\n',name,re.S)[0]
    con = tree.xpath('(.//p[@class="lead"])[1]/span/text()')[1]
    con  = con.translate(font_map)
    print(name)
    print(con)

