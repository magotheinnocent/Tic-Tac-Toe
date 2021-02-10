# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = [x for x in old_list if old_list > 0]
print(binary_list)
