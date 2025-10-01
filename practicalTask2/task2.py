import math
x = int(input())
y = int(input())
z = int(input())
numerator = (x**5 + 9) / abs(-8) * y
cube_root = numerator ** (1/3)
denominator = 7 - (z % y)

if denominator == 0:
    print("Ошибка: деление на ноль")
else:
    a = cube_root / denominator
    result = round(a, 3)
    print(result)