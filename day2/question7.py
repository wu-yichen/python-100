

result = []


def convert_to_two_dimension(x, y):
    for i in range(0, x):
        sub_list = []
        for j in range(0, y):
            sub_list.append(i * j)
        result.append(sub_list)


convert_to_two_dimension(3, 5)
print(result)
