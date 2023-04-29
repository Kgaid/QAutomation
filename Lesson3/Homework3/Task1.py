palindrom = input('Please enter any word: ')
if str(palindrom) == str(palindrom)[::-1]:
    print("+")
else:
    print("-")
