# Task 1
num1 = int(input('Prompt your desire number one: '))
num2 = int(input('Prompt your desire number two: '))
operations = input('What do you wanna do with numbers: + or - or * or / or // or % or ** 1: ')
if operations == '+':
    print(f"Result of operation is {num1 + num2}")
elif operations == '-':
    print(f"Result of operation is {num1 - num2}")
elif operations == '*':
    print(f"Result of operation is {num1 * num2}")
elif operations == '/':
    resultOfDivide = round(num1 / num2, 2)
    print("Result of operation is " + str(resultOfDivide))
elif operations == '//':
    print(f"Result of operation is {num1 // num2}")
elif operations == '%':
    print(f"Result of operation is {num1 % num2}")
elif operations == '**':
    print(f"Result of operation is {num1 ** num2}")
if num1 >= num2:
    if num1 > num2:
        print("Number 1 is greater than Number 2")
    elif num1 == num2:
        print("Number 1 is equal Number 2")
if num1 <= num2:
    if num1 < num2:
        print("Number 1 is less than Number 2")
    elif num1 != num2:
        print("Number 1 is not equal to Number 2")
