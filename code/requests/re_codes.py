import requests

response = requests.get('http://httpbin.org')
print(response.status_code)
print(requests.codes.locked)
if response.status_code == requests.codes.ok:
	print('访问成功！')