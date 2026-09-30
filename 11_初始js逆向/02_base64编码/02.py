import execjs

str='Fu zhun da ren xia wu hao'
with open('02.js',encoding='utf-8') as f:
    cry = execjs.compile(f.read())
    print(cry.call('base64_encode',str))