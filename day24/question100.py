list1 = ["bcdef", "abcdefg", "bcde", "bcdef"]

dic = {}

for i in list1:

    dic[i] = dic.get(i, 0) + 1

print(" ".join([str(i) for k, i in dic.items()]))
