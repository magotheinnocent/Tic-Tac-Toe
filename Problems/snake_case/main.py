word = input()

for i in range(len(word)):
    if not word[i].islower() and i > 0:
        word = word[:i] + "_" + word[i:]
    print(word)