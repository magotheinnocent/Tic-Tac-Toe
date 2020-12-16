value_of_index = float(input())

if value_of_index < 2:
    print("Analytic")

elif value_of_index <= 3:
    print("Synthetic")

else:
    print("Polysynthetic")