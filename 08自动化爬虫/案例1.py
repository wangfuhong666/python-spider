import csv
from DrissionPage._pages.chromium_page import ChromiumPage


page=ChromiumPage()
page.get('https://top.chinaz.com/hangye/')
page.set.timeouts(5)
ul=page.ele('.listCentent')
lis=ul.eles("x:./li")
head=["网站名字","域名","简介","排名","得分"]
sumlist =[]
for li in lis:
    name=li.ele('x:.//h3[@class="rightTxtHead"]/a').text
    url = li.ele('x:.//h3[@class="rightTxtHead"]/span').text
    rank = li.ele('x:.//div[@class="RtCRateCent"]/strong').text
    score= li.ele('x:.//div[@class="RtCRateCent"]/span').text
    new_page = li.ele('x:.//h3[@class="rightTxtHead"]/a').click.for_new_tab()
    con = new_page.ele('x:.//div[@class="Centright fr SimSun"]/p').text
    new_page.close()
    print(name)
    print(url)
    print(con)
    print(rank)
    print(score)
    sumlist.append([name,url,con,rank,score])
with open(' 站长之家.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(head)
    writer.writerows(sumlist)
page.close()

