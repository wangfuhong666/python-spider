from DrissionPage._pages.chromium_page import ChromiumPage
import time
import csv
page=ChromiumPage()
page.get("https://stats.ioinformatics.org/results/2025")
for _ in range(5):
    page.run_js('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
di = page.ele('x:.//div[@class="maincontent"]')
tr = di.eles('x: ./table/tbody/tr')
print(len(tr))
head = ["contestant","member","score_abs","score_rel","award"]
with open("IOI2025.csv",'w',encoding='utf-8',newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(head)
    for li in tr[2:]:
        time.sleep(1)
        contestant = li.ele('x:.//td[2]/a').text
        member = li.ele('x:.//td[3]/a').text
        score_abs = li.ele('x:.//td[10]').text
        score_rel = li.ele('x:.//td[11]').text
        award = li.ele('x:.//td[12]').text
        print(contestant,member,score_abs,score_rel,award)
        writer.writerow([contestant,member,score_abs,score_rel,award])
page.close()