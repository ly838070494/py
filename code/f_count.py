def createCounter():
    s = [0]
    def counter():
        s[0] += 1
        return s[0]
    return counter
