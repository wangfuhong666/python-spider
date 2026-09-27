import requests
from lxml import etree
import csv
class Spider:
    def __init__(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Proxy-Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",

        }
        self.sum_list=[
            ["女装品牌","所在地区","图片链接"]
        ]

    def get_res(self):
        response = requests.get("http://nz.efu.com.cn/brand/nz/list-2.html", headers=self.headers, verify=False)
        return response.text
        #print(response.text)
    def get_html(self,res):
        tree=etree.HTML(res)
        data=tree.xpath("//div[@class='photo-lst']//li")

        for li in data:
            #m名称
            a1=li.xpath('.//div["txtCon-a"]/a/text()')[0]
            # print(a1)
            #所在地区
            a2 = li.xpath('.//div["txtCon-a"]/p/text()')[0].replace('所在地区：', '')
            #print(a2)
            #图片链接
            a3 = li.xpath('.//a["sw-ui-photo120-box"]/img/@src')[0]
            #print(a3)
            self.sum_list.append([a1,a2,a3])
        #print(self.sum_list)
    def csv_writer(self):
        with open("xpath实战.csv",'w',newline='',encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.sum_list)
    def run(self):
        res=self.get_res()
        self.get_html(res)
        self.csv_writer()
spider = Spider()
spider.run()
