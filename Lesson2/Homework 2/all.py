# first task 1

# x = int(input('Please write the temperature in Celsius: '))
#
# fahrenheit = str((x+32) * 5/9)
# kelvin = str(x + 273.16)
# print("Fahrenheit =" + fahrenheit + "F", "Kelvin =" + kelvin + "K", sep='\n')

# ------------------------------------------------------------
# second task 2
#
# v1 = float(input('Please enter first volume: '))
# v2 = float(input('Please enter second volume: '))
# t1 = float(input('Please enter first temperature: '))
# t2 = float(input('Please enter second temperature: '))
# vol = v1 + v2
# temp = str((v1*t1 + v2*t2) / vol)
# vol = str(vol)
# print("Temperature =" + temp + "C", "Volume =" + vol + "l")


# ------------------------------------------------------------
# third task 3

# currency = input ('Please enter currency you have. UAH or USD, EUR:')
# fin_cur = input('Please enter currency you would like to receive. UAH or USD,EUR:')
# x = int(input("Please enter quantity: "))
# if currency == 'UAH' and fin_cur == 'USD' and x > 0:
#     x = str(x * 0.027)
#     print(x + "USD")
# elif currency == 'UAH' and fin_cur == 'EUR' and x > 0:
#     x = str(x * 0.024)
#     print(x + "EUR")
# elif currency == 'EUR' and fin_cur == 'UAH' and x > 0:
#     x = str(x * 40.84)
#     print(x + "UAH")
# elif currency == 'EUR' and fin_cur == 'USD' and x > 0:
#     x = str(x * 1.11)
#     print(x + "USD")
# elif currency == 'EUR' and fin_cur == 'USD' and x > 0:
#     x = str(x * 1.11)
#     print(x + "USD")
# elif currency == 'USD' and fin_cur == 'EUR' and x > 0:
#     x = str(x * 0.90)
#     print(x + "EUR")
# elif currency == 'USD' and fin_cur == 'UAH' and x > 0:
#     x = str(x * 36.78)
#     print(x + "UAH")
# elif x <= 0:
#     print('Please enter only POSITIVE number')
# else:
#     print('This was not included in the task. Please enter UAH, USD or EUR.')

# uahusd = x * 0.027
# usduah = x * 36.78
# uaheur = x * 0.024
# euruah = x * 40.84

# -------------------------------------------------------------------
# fourth task

# number1 = input("Enter the first number:")
# number2 = input("Enter the second number:")
# if float(number2) == 0:
#     print('Error: division by zero')
#     exit()
# operation = input("Please enter operation: +,-,* or /")
# match operation:
#     case '+':
#         print(float(number1) + float(number2))
#     case '-':
#         print(float(number1) - float(number2))
#     case '*':
#         print(float(number1) * float(number2))
#     case '/':
#         print(float(number1) / float(number2))
#
