numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number = input()
for _i in range(len(number)):
    print(numbers[int(number[_i])])