import requests
response = requests.get('https://sls.cdb.com.cn/')
print(response.status_code)