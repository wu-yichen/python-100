input = "Hello world!"
# upper_count = 0
# lower_count = 0
# for ch in input:
#     if ch.isupper():
#         upper_count += 1
#     elif ch.islower():
#         lower_count += 1

# print(f"upper case are: {upper_count} lower case are: {lower_count}")

upper_count = sum(1 for i in input if i.isupper())
lower_count = sum(1 for i in input if i.islower())
print(f"upper case are: {upper_count} lower case are: {lower_count}")
