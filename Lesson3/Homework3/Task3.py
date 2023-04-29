word = input(str('Please enter any String: '))
result = word.find('abc', 0, 3)
result1 = word.replace('abc', 'www')
if result == 0:
     print(result1)
else:
    new_word = word[0:] + 'zzz'
    print(new_word)
