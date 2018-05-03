import urllib.parse
import urllib.request

import json

data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
#print(data)  
#b'word=hello'
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
d = json.loads(response.read().decode('utf-8')) #把str转换成dict
print(type(d))
print(d['origin'])
