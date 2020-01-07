import math


x = 0
y = 0
while True:
    op = input("please give operation: ").split()
    if not op:
        break

    direction, steps = map(str, op)
    if direction == "UP":
        y += int(steps)
    elif  direction == "DOWN":
        y -= int(steps)
    elif direction == "LEFT":
        x -= int(steps)
    elif direction == "RIGHT":
        x += int(steps)

distance = round(math.sqrt(y ** 2 + x ** 2))

print(distance)
