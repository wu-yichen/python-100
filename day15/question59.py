
n = input("please input the number: ")
result = 0.0

# for index, num in enumerate(range(int(n))):
#     fac = int(index)
#     result += (fac+1)/(fac+2)
#print(str(round(result, 2)))


for i in range(1, int(n)+1):
    result += float(i)/float(i+1)

print(round(result, 2))
