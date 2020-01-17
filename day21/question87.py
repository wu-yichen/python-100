list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]

print([i for i in list1 if i in [i for i in list2]])


set1 = set(list1)
set2 = set(list2)

set1 &= set2

print(list(set1))
