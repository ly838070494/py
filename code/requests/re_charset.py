import requests as re

response = re.get('https://www.baidu.com')
response.encoding = 'utf-8' #解决乱码问题
print(response.text) 