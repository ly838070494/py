import urllib.parse

params = {
	'name':'zhaofeng',
	'age':20
}
base_url = 'http://www.baidu.com'

url = base_url+'?'+urllib.parse.urlencode(params)
print(url)