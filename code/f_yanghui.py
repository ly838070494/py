def yanghui():
    ret = [1]
    while True:
        yield ret
        L = ret.copy()
        for x in range(1, len(ret)):
            ret[x] = L[x-1] + L[x]
        ret.append(1)
