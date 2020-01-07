import re

psw = input("please input password: ").split(",")

result = []
for item in psw:
    
    if len(item) < 6 or len(item) > 12:
        continue
    elif not re.search("[a-z]", item):
        continue
    elif not re.search("[A-Z]", item):
        continue
    elif not re.search("[0-9]", item):
        continue
    elif not re.search("[$#@]", item):
        continue

    result.append(item)

print("".join(result))
