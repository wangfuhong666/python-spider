import csv
import time
from DrissionPage._pages.chromium_page import ChromiumPage
page = ChromiumPage()
page.get('https://www.suning.com/')
page.ele('#searchKeywords').input("书籍")
page.ele('#searchSubmit').click()
time.sleep(5)
for _ in range(5):
    page.run_js('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)

lis=page.eles('x:.//ul[@class="general clearfix"]/li')
head =['书籍名称','价格','评价数']
sum = []

for li in lis:
    name = li.ele('x: .//div[@class="title-selling-point"]/a').text
    price = li.ele('x:.//div[@class="price-box"]/span').text
    num = li.ele('x:.//div[@class="info-evaluate"]/a/i').text

    print(name.split()[0])
    print(price)
    print(num)
    sum.append([name.split()[0],price,num])
with open('苏宁易购.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(head)
    writer.writerows(sum)
page.close()