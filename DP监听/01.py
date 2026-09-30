from DrissionPage import Chromium

chrome = Chromium()

tab = chrome.latest_tab

tab.listen.start('explore/all')#括号里面·填数据包特征

tab.get('https://gitee.com/explore/all?order=starred&page=1')

tab.wait(1)

for _ in range(5):

    tab.ele('@rel=next').click()

    res = tab.listen.wait()#等待或获取数据包

    print(res.url)

    print(res.response.body)#获取响应体
for packer  in tab.listen.steps():
    print(packer.url)
    tab.ele('@rel=next').click()
    if int(packer.url[-1:]) >=9:
        break
