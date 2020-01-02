input = 'hello world! 123'

num_count = 0
letter_count = 0

for c in input:
   # print(c)
    if c.isdigit():
        num_count += 1
    elif c.isalpha():
        letter_count += 1

print(num_count, letter_count)
