import requests

#查看User-Agent，浏览器输入chrome://version
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360EE'
}
response = requests.get('http://www.zhihu.com', headers=headers)
print(response.text)