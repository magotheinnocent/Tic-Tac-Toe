
for i in range(1, 101):
    if i % 3 == 0:
        print(i)
        print("Fizz")
    elif i % 5 == 0:
        print(i)
        print("Buzz")
    elif i % 5 == 0 and i % 3 == 0:
        print(i)
        print("FizzBuzz")
