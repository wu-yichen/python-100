input_list = [str(num) for num in range(1000, 3001)]

result = list(filter(lambda num: all(ord(n) %
                                     2 == 0 for n in num), input_list))


# result = []
# for num in range(1000, 3001):
#     is_even = True
#     for digit in map(int, str(num)):
#         if digit % 2 != 0:
#             is_even = False
#             break
#     if is_even:
#         result.append(str(num))

print(','.join(result))
