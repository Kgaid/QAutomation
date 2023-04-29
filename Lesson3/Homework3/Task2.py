frase = input(str('Please enter a frase: '))
frase = frase.lower()
word = input(str('Please enter in lowercase a word to be searched in the frase: '))
result = frase.find(word)
if result >= 0:
    print('YES')
else:
    print('NO')
