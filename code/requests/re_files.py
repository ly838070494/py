import requests

files = {
	'files':open('test.jpg', 'rb')
}

response = requests.post('http://httpbin.org/post', files = files)
print(response.text)