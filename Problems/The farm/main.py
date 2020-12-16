price = int(input())
chicken = price / 23
goat = price / 678
pig = price / 1296
cow = price / 3848
sheep = price / 6769

if price < 23:
    print("None")

elif price < 678:
    if price // 23 > 1:
        print(f"{int(chicken)} chickens")
    else:
        print(f"{int(chicken)} chicken")


elif price < 1296:
    if price // 678 > 1:
        print(f"{int(goat)} goats")
    else:
        print(f"{int(goat)} goat")

elif price < 3848:
    if price // 1296 > 1:
        print(f"{int(pig)} pigs")
    else:
        print(f"{int(pig)} pig")

elif price < 6769 and cow > 1:
    if price // 3848 > 1:
        print(f"{int(cow)} cows")
    else:
        print(f"{int(cow)} cow")

else:
    if price // 23 > 1:
        print(f"{int(sheep)} sheep")
    else:
        print(f"{int(sheep)} sheep")
