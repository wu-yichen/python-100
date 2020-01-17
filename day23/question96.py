def compute(string, num):
    for index, ch in enumerate(string):
        if index % num == 0:
            print()
        print(ch, end="")


compute("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)
