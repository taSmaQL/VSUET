num1 = 67
num2 = 69
digits = []
suggestion = input('D you wanna number 1 or number2 (num1/num2)?: ')
if suggestion == "num1":
    while num1 > 0:
        remainder = num1 % 10
        digits.append(remainder)
        num1 //= 10
if suggestion == "num2":
    while num2 > 0:
        remainder = num2 % 10
        digits.append(remainder)
        num2 //= 10
digits.reverse()
print(f"Sum of digits of number either 1 or 2 is {digits[0] + digits[1]} and multiple of number either 1 or 2 is {digits[0] * digits[1]}")
