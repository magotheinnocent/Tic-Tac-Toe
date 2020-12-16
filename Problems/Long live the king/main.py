column = int(input())
row = int(input())

if (column == 1 and row == 1) or (column == 8 and row == 1) or (column == 8 and row == 8) or (column == 1 and row == 8):
    print("3")

elif (column == 1 and 1 < row < 8) or (row == 1 and 1 < column < 8) or (column == 8 and 1 < row < 8) or (row == 8 and 1 < column < 8):
    print("5")

else:
    print("8")