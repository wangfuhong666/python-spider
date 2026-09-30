url = ""
# 导入请求模块
import requests
# 引进请求头（伪装）（注意检查有没有cookie）
headers={'user-agent':'','referer':''}
# 使用request
response = requests.get(url, headers=headers)
open("7.mp4", 'wb').write(response.content)