import re

content = "Extra things hello 123455 World_this is a regex Demo extra things"

content = re.sub('(\d+)',r'\1 44444', content) #\1代表前一个匹配项123455 匹配项必须加括号
print(content)