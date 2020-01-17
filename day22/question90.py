string = "abcdefgabc"

dic = {}

for ch in string:
    if ch not in dic:
        dic[ch] = 1
    else:
        dic[ch] += 1

sorted(dic.items(), key=lambda item: item[1])
print(dic)
