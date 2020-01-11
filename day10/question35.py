def print_last_five():
    list = [item ** 2 for item in range(1, 21)][-5:]
    print(list)


print_last_five()
