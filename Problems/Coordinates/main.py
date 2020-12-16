number1 = input()
number2 = input()

if float(number1) == 0.0 and float(number2) == 0.0:
    print("Origin")

elif float(number1) > 0.0 and float(number2) > 0.0:
    print("I")

elif float(number1) < 0.0 and float(number2) > 0.0:
    print("II")

elif float(number1) < 0.0 and float(number2) < 0.0:
    print("III")

else:
    print("IV")