from DrissionPage import ChromiumPage
import time
page = ChromiumPage()
url = "https://www.shiguangtongxue.cn/"
page.get(url)
page.ele("#loginAccountInput").input("装饰器残响")
time.sleep(2)
page.ele("#loginPasswordInput").input("1q2w3e4r")
time.sleep(2)
page.ele("#loginSubmitButton").click()
time.sleep(5)
page.ele('x:.//a[@class="subject-card subject-card-shortcut subject-card-beta"]').click()
time.sleep(5)
full_dom_html = page.html
with open("elements.html","w",encoding="utf-8") as f:
    f.write(full_dom_html)
page.ele('x:.//div[@class="dialog-footer"][2]/button').click(by_js=True)
# ✅获取 Elements面板完整渲染后的html（等价F12 Elements全部代码）
#full_dom_html = page.html

# 保存到文件，encoding="utf‑8"避免gbk报错
#with open("elements.html","w",encoding="utf-8") as f:
#    f.write(full_dom_html)

# 选取元素示例，xpath/css选择器
# ele = page.ele('x://div[@class="xxx"]') # xpath定位元素
# print(ele.text)
# print(ele.attr("class")) #拿属性

page.quit()
