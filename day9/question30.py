#str = lambda str1, str2: print(str1) if len(str1) > len(str2) else print(str1, str2) if len(str1) == len(str2) else print(str2)

str = lambda str1, str2: print(max(str1, str2, key=len)) if len(str1) != len(str2) else print(str1, str2)

str("he", "llo")
str("he", "ll")
str("hel", "lo")
