path = r'c:/python/README.md'
with open(path, 'r') as f:
    s = f.read()
    print(s)

#write
path = r'c:/python/code/file.txt'
with open(path, 'w') as f:
    f.write('hi python')
