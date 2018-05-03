import requests

# response = requests.get('http://httpbin.org/get')
response = requests.post('http://httpbin.org/post')
# response = requests.head('http://httpbin.org/headers')
# response = requests.put('http://httpbin.org/put')
#response = requests.delete('http://httpbin.org/delete')
#response = requests.options('http://httpbin.org/get')
print(response.content.decode('utf-8'))