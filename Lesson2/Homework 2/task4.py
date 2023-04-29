number1 = input("Enter the first number:")
number2 = input("Enter the second number:")
if float(number2) == 0:
    print('Error: division by zero')
    exit()
operation = input("Please enter operation: +,-,* or /")
match operation:
    case '+':
        print(float(number1) + float(number2))
    case '-':
        print(float(number1) - float(number2))
    case '*':
        print(float(number1) * float(number2))
    case '/':
        print(float(number1) / float(number2))
