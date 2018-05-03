import requests
from requests.packages import urllib3

urllib3.disable_warnings()

response = requests.get('http://www.12306.cn/mormhweb', verify=False)
print(response.text)