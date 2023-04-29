text = input(str('Enter here some text:')).split()
if len(text) < 3:
    print('Please enter at least 3 words, current quantity of words:  ' + str(len(text)))
else:
    print(text[-3:])
