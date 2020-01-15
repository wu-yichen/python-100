def gen(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i


for i in gen(10):
    print(i)
