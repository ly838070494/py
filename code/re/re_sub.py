import re

content = "Extra things hello 123455 World_this is a regex Demo extra things"

content = re.sub('\d+','', content) #把content中数字替换成空
print(content[:21])