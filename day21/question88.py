list1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

# for i in list1:
#     if list1.count(i) > 1:
#         list1.remove(i)

# print(list1)

dic = {}

for i in list1:
    if i not in dic:
        dic[i] = True

print(list(dic))
