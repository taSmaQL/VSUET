# 1.1
import math
x = int(input(("Number: ")))
if x>=0:
    print(round(math.sqrt(x) + pow(x,2),1))
if x<0:
    print(round(1/x,2))


# 1.2
'''
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))

if a > b:
    print("Максимальное число:", a)
    print("Минимальное число:", b)
else:
    print("Максимальное число:", b)
    print("Минимальное число:", a)
'''