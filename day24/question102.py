input_str = "Hello321Bye360"

dic = {}
for ch in input_str:
    if ch.isdigit():
        dic["Digit"] = dic.get("Digit", 0) + 1
    else:
        dic["Letter"] = dic.get("Letter", 0) + 1

for k, v in dic.items():
    print(f"{k} - {v}")
