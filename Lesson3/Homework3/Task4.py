email = input(str('Please enter an email for validation: '))
at = email.find('@')
dot = email.find('.')
if at >= 0 and dot >= 0:
    print('YES')
else:
    print('NO')
