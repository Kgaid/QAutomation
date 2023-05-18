def change_list(element):
    if len(element) >= 2:
        element[0], element[-1] = element[-1], element[0]
        return element
    else:
        return print("Please enter at least 2 words/numbers")
