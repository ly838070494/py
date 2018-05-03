import requests

from requests.exceptions import ReadTimeout, ConnectionError, RequestException

try:
	response = requests.get('http://httpbin.org/get', timeout=0.01)
	print(response.status_code)
except ReadTimeout:
	print('time out')
except ConnectionError:
	print('conncetion error')
except RequestException as e:
	print(e.reason)