import requests

"""
      目标网站  http://www.ccgp-hunan.gov.cn/page/notice/more.jsp
"""
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
   'referer':'http://www.ccgp-hunan.gov.cn/'
}
a=int( input('你要爬几页数据'))
url = 'http://www.ccgp-hunan.gov.cn/mvc/getNoticeList4Web.do'
for j in range(1, a+1):
    # 1.明确目标
    data = {
        'pType': '',
        'prcmPrjName': '',
        'prcmItemCode': '',
        'prcmOrgName': '',
        'startDate': '2025-01-01',
        'endDate': '2025-12-02',
        'prcmPlanNo': '',
        'page': f'{j}',
        'pageSize': '18'
    }

    # 2。发起请求，接受响应
    res = requests.post(url, headers=headers, data=data)
    # print(res.json())
    # 3.数据解析
    for i in res.json()['rows']:
        AREA_NAME = i['AREA_NAME']
        NEWWORK_DATE = i['NEWWORK_DATE']
        ORG_CODE = i['ORG_CODE']
        NOTICE_NAME = i['NOTICE_NAME']
        PRCM_MODE_NAME = i['PRCM_MODE_NAME']
        NOTICE_TITLE = i['NOTICE_TITLE']
        # 4，数据存储
        with open(f"信息公开{a}页.txt", 'a', encoding='utf-8') as f:
            f.write('\n'.join([AREA_NAME, NEWWORK_DATE, ORG_CODE, NOTICE_NAME, PRCM_MODE_NAME, NOTICE_TITLE]) + '\n\n')
        # print(AREA_NAME,NEWWORK_DATE,ORG_CODE,NOTICE_NAME,PRCM_MODE_NAME,NOTICE_TITLE)


