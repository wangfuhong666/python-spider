from DrissionPage._configs.chromium_options import ChromiumOptions
from DrissionPage._pages.chromium_page import ChromiumPage

#方法一

import time

#创建浏览器对象
page=ChromiumPage()
page.set.timeouts(5)
#告诉浏览器打开的网址是哪个(方法get)
page.get('https://www.baidu.com')
time.sleep(2)
#从网址里面获取需要的数据
#定位网页标签元素
#浏览器对象.ele()找一个标签
#浏览器对象.eles()找多个标签
'''
    ele的函数调用
    1.标签名字 page.ele('title') (不推荐) 推荐里面'tag:标签名字'
    2.css选择器 .class 与#id    page.ele('#chat-textarea')
    3.xpath定位 'xpath:语法' or 'x:语法'
    4.标签属性 '@属性名=属性值(属性值不需要加引号)'
'''
#print(type('tag:title'))
# print(page.eles('tag:div'))
# print(page.ele('#chat-textarea'))
# print(page.ele('.=chat-input-textarea chat-input-scroll-style'))
# print(page.ele('xpath://*[@class="chat-input-textarea chat-input-scroll-style"]'))
#获取标签内容 标签对象.text
#获取标签属性 标签对象.attr
#获取标签多个属性 标签对象.attrs
#print(page.ele('x://title').text)
#print(page.ele('#chat-textarea').attr('data-ai-placeholder'))
#print(page.ele('#chat-textarea').attrs['placeholder'])
#标签对象.click()点击这个标签
#标签对象.input(文本)在标签中输入内容
#设置时限。1.在查找的函数·里面加timeout参数 2.page.set.timeouts()设置全局最长等待时间
page.ele('#chat-textarea').input("周杰伦")
#time.sleep(2)
page.ele('#chat-submit-button').click()

#存储数据

#关闭浏览器
time.sleep(2)
#page.close()

'''
#方法一用不了用方法二
chrome_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
#创建一个浏览器的配置对象
opts=ChromiumOptions()
#将路经放到配置对象当中
opts.set_browser_path(chrome_path)
#然后接方法一即可
'''