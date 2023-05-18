def func_exp2(n):
    if n == 0:
        return "no"
    while n != 1:
        if n % 2 != 0:
            return "no"
        n = n // 2
    return "yes"
