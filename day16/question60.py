def compute(n):
    if n == 0:
        return 0

    return compute(n-1) + 100


print(compute(5))
