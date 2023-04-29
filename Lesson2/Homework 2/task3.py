currency = input ('Please enter currency you have. UAH or USD, EUR:')
fin_cur = input('Please enter currency you would like to receive. UAH or USD,EUR:')
x = int(input("Please enter quantity: "))
if currency == 'UAH' and fin_cur == 'USD' and x > 0:
    x = str(x * 0.027)
    print(x + "USD")
elif currency == 'UAH' and fin_cur == 'EUR' and x > 0:
    x = str(x * 0.024)
    print(x + "EUR")
elif currency == 'EUR' and fin_cur == 'UAH' and x > 0:
    x = str(x * 40.84)
    print(x + "UAH")
elif currency == 'EUR' and fin_cur == 'USD' and x > 0:
    x = str(x * 1.11)
    print(x + "USD")
elif currency == 'EUR' and fin_cur == 'USD' and x > 0:
    x = str(x * 1.11)
    print(x + "USD")
elif currency == 'USD' and fin_cur == 'EUR' and x > 0:
    x = str(x * 0.90)
    print(x + "EUR")
elif currency == 'USD' and fin_cur == 'UAH' and x > 0:
    x = str(x * 36.78)
    print(x + "UAH")
elif x <= 0:
    print('Please enter only POSITIVE number')
else:
    print('This was not included in the task. Please enter UAH, USD or EUR.')