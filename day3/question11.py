import sys

input = sys.argv[1].split(',')

for num in input:
    int_num = int(num, 2)
    if int_num % 5 == 0:
        print("{0:b}".format(int_num))
