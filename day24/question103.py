# sum = 0


# def compute(n):
#     global sum
#     if n == 0:
#         return sum
#     sum += n
#     return compute(n-1)


def compute(n):
    if n == 0:
        return n
    return n + compute(n-1)


print(compute(5))
