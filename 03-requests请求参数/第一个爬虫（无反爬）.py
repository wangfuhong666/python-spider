url = "https://aisearch.cdn.bcebos.com/homepage/dashboard/ai_reading/icon/word.png"
# 导入请求模块
import requests

# 使用request
response = requests.get(url)
# 打开空视频并写进去
open("4.png", "wb").write(response.content)
