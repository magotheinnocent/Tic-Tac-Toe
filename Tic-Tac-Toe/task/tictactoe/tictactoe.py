# write your code here
number = str(input("Enter cells:"))

print("---------")
print(f"| {number[0]} {number[1]} {number[2]} |")
print(f"| {number[3]} {number[4]} {number[5]} |")
print(f"| {number[6]} {number[7]} {number[8]} |")
print("---------")

x_win = {number[0]} == {number[1]} == {number[2]} == "X" or {number[3]} == {number[4]} == {number[5]} == "X" or {number[6]} == {number[7]} == {number[8]} == "X"
o_win = {number[0]} == {number[1]} == {number[2]} == "O" or {number[3]} == {number[4]} == {number[5]} == "O" or {number[6]} == {number[7]} == {number[8]} == "O"

if x_win:
    print("X wins")

elif o_win:
    print("O wins")


