from DrissionPage import Chromium
import time
chrome = Chromium()
tab = chrome.latest_tab
tab.get("https://www.baidu.com")
tab.set.window.max()
tab.wait(1,2)

tab.ele("#chat-textarea").input("三国杀")

#tab.close()

