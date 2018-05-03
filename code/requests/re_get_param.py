import requests

data = {
	'name':'zhaofan',
	'age': 20
}
response = requests.get('http://httpbin.org/get', params=data)
print(response.url)
print(response.content.decode('utf-8'))