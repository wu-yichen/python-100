input = "1,2,3,4,5,6,7,8,9"

result = [int(num)**2 for num in input.split(",") if int(num) % 2 != 0]
print(result)
