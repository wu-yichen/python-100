num_list = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        # num_list.append(str(num))
        print(num, end=',')

# print(','.join(num_list))
print()
