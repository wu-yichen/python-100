# def fib(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     return fib(n-1) + fib(n-2)


def fib(n):

    result = []

    for i in range(0, n+1):
        if i == 0 or i == 1:
            result.append(i)
            continue
        result.append(result[i-1] + result[i-2])
    return result[n]


print(fib(7))
