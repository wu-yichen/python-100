li = []

while True:
    val = input("please give the name, age and score: ").split()
    if not val:
        break
    name, age, score = map(str, val)
    li.append((name, age, score))

new_list = sorted(li, key=lambda item: (item[0], item[1], item[2]))

print(new_list)
