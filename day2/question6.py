import math

input = "100, 150, 180"
result = []
for num in input.split(','):

    result.append(str(math.floor(math.sqrt((2 * 50 * int(num)) / 30))))

print(','.join(result))
