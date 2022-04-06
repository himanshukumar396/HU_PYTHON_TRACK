def fin(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


ln = int(input('How long? '))
print(list(fin(ln)))