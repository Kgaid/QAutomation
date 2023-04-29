class FormulaError(Exception):
    pass


while True:
    try:
        operation = input("Please enter operation like sample 1 + 1: ")
        symbols = operation.split()
        if len(symbols) != 3:
            raise FormulaError("The format is incorrect")
        a = float(symbols[0])
        b = float(symbols[2])
        if symbols[1] not in ['+', '-']:
            raise FormulaError("Incorrect operands")
    except ValueError:
        raise FormulaError('Incorrect value')
    except FormulaError as fe:
        print(f'Error: {fe}')
        continue
    if symbols[1] == '+':
        solution = a + b
    else:
        solution = a - b
    print(f"The solution is: {solution}")
