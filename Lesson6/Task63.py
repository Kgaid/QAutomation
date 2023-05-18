class MyError(Exception):
    pass
def is_prime(a):
    try:
        a = int(a)
        if 2 <= a <= 1000:
            return True
        else:
            if 2 > a or a > 1000:
                raise MyError("False")
    except MyError:
        return False
    except ValueError:
        print("Error type of value! Please enter any number")
