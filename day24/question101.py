input_str = "aabbbccde"

dic = {}
for ch in input_str:
    dic[ch] = dic.get(ch, 0) + 1

for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True):
    print(k, v)
