user_input = input("please input: ")

input_list = user_input.split(" ")

print([item for item in input_list if str(item).isdigit()])
