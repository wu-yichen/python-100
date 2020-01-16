import timeit

t = timeit.Timer("for i in range(100): 1+1")

print(t.timeit())
