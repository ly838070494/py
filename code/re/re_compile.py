import re
content= """hello 12345 world_this
123 fan
"""

pattern =re.compile("hello.*fan",re.S) #将正则表达式编译成正则表达式对象，方便复用该正则表达式

result = re.match(pattern,content)
print(result)
print(result.group())