import execjs

with open('01.js', "r",encoding='utf-8') as f:
    js_code = f.read()
    cry = execjs.compile(js_code)
    print(cry.call('a'))