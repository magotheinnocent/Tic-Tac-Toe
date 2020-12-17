camelword = input()
snakeword = camelword[0].lower()

for letter in camelword[1:]:
    if letter.isupper():
        snakeword += "_" + letter.lower()
    else:
        snakeword += letter

print(snakeword)