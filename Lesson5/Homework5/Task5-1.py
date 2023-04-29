import math

class DiscriminantError(Exception):
    pass


print("введите коэффициенты для уравнения: ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c

if discr < 0:
    raise DiscriminantError("корней нет")
elif discr == 0:
    x = -b /(2*a)
    print("уравнение имеет один корень", x)

else:
    x1 = (-b + math.sqrt(discr))
    x2 = (-b - math.sqrt(discr))
    print("уравнение имеет 2 корня", x1, x2)

