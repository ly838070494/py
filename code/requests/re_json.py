import requests
import json

response = requests.get('http://httpbin.org/get')
print('******** response.json() **********')
print(type(response.json()))
print(response.json())
print('******** json.loads(response.text) ***********')
print(type(json.loads(response.text)))
print(json.loads(response.text))