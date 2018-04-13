def move(n, x, y, z):
    if n == 1:
        print(x, '--->', z)
    if n > 1:
        move(n-1, x, z, y)
        move(1, x, y, z)
        move(n-1, y, x, z)

