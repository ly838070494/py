import os
def search(str, path='.'):
    for x in os.listdir(path):
        #print(x)
        if os.path.isfile(os.path.join(path, x)) and (str in x):
            print('found!', os.path.join(path, x))
        if os.path.isdir(os.path.join(path, x)):
            search(str, os.path.join(path, x))

search('print', r'c:/python')
