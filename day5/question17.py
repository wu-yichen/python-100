total = 0

while True:
    string = input('please enter: ').split()
    if not string:
        break

    op, num = map(str, string)
    if op == "D":
        total += int(num)
    elif op == "W":
        total -= int(num)

print(total)
