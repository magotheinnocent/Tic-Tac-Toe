number1 = int(input())
number2 = int(input())

if number1 == 0 and number2 == 0:
    print("Origin")

elif number1 > 0 and number2 > 0:
    print("I")

elif number1 < 0 and number2 > 0:
    print("II")

elif number1 < 0 and number2 < 0:
    print("III")

else:
    print("IV")