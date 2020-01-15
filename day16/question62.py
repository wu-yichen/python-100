def fib(n):
    result = []
    for i in range(0, n+1):
        if i == 0 or i == 1:
            result.append(i)
            continue
        result.append(result[i-1]+result[i-2])
    return result


print(fib(7))
