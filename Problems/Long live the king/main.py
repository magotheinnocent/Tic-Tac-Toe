column = int(input())
row = int(input())

if row in (1, 8) and column in (1, 8):
    print("3")

elif column in (1, 8) and row in(1, 8):
    print("5")

else:
    print("8")