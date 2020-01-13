input_str = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda item: item ** 2, filter(lambda item: item % 2 == 0, input_str))))
