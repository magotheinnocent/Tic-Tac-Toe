a = int(input())
b = int(input())
mod = []
for i in range(1, 101):
    if i % 3 == 0:
        print(mod.append(i))
        print("Fizz")
    elif i % 5 == 0:
        print(mod.append(i))
        print("Buzz")
    elif i % 5 == 0 and i % 3 == 0:
        print(mod.append(i))
        print("FizzBuzz")
