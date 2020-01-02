# again and hello makes perfect practice world
input = 'hello world and practice makes perfect and hello world again'

input_list = input.split(' ')

result = set()

for word in input_list:
    result.add(word)

new_list = list(result)

reverse_sorted_list = sorted(new_list[::-1])

print(' '.join(reverse_sorted_list))
