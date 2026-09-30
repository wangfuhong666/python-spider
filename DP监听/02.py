from DrissionPage import Chromium,ChromiumOptions
from loguru import logger
co = ChromiumOptions()
co.incognito(True)
chrome = Chromium(addr_or_opts=co)
chrome.set.timeouts(3)
tab = chrome.latest_tab

tab.listen.start('api/zlsm/getInfo')#括号里面·填数据包特征

tab.get('https://zldj.cde.org.cn/list?listType=PatentStatementList')
#api/zlsm/getList
tab.wait.eles_loaded('查看')
for i in range(1,11):
    tab.ele(f'x:.//tbody/tr[{i}]//button').click()
    tab.wait.eles_loaded('药品名称')
    tab.wait(1, 2)
    tab.ele('关 闭').click(by_js=True)
    tab.wait(0,1)
#设置等待时间
for packet in tab.listen.steps(timeout=5):
    logger.info(packet.response.body)
chrome.quit()