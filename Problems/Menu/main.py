pizza = ("Margherita", "Four Seasons", "Neapolitan", "Vegetarian", "Spicy")
salad = ("Caesar salad", "Green salad", "Tuna salad", "Fruit salad")
soup = ("Chicken soup", "Ramen", "Tomato soup", "Mushroom cream soup")

choice = input()

if choice == 'pizza':
    print(*list(pizza), sep=', ')


elif choice == 'salad':
    print(*list(salad), sep=', ')

elif choice == 'soup':
    print(*list(soup), sep=', ')

else:
    print("Sorry, we don't have it in the menu")