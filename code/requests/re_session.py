import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/abc/hello')
response = s.get('http://httpbin.org/cookies')

print(response.text)