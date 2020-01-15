def compute(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i


result = []
for i in compute(100):
    result.append(str(i))

print(",".join(result))
