# put your python code here
number_1 = float(input())
number_2 = float(input())
arithmetic = input()

if number_2 == 0.0 and arithmetic in ("/", "mod", "div"):
    print("Division by 0!")

elif arithmetic == "+":
    print(number_1 + number_2)

elif arithmetic == "*":
    print(number_1 * number_2)

elif arithmetic == "pow":
    print(number_1 ** number_2)

elif arithmetic == "-":
    print(number_1 - number_2)

elif arithmetic == "mod":
    print(number_1 % number_2)

elif arithmetic == "/":
    print(number_1 / number_2)

elif arithmetic == "div":
    print(number_1 // number_2)

else:
    print("Choose another arithmetic sign")
