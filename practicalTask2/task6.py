import math
m = -5
n = 10
a = int(input('Prompt your desire positive number one: '))
b = int(input('Prompt your desire positive number two: '))
c = int(input('Prompt your desire positive number three: '))
disc = b**2 - 4 * a * c
sqrt_val = math.sqrt(abs(disc))
sqrt1 = round(((-b + sqrt_val)/(2*a)),2)
sqrt2 = round(((-b - sqrt_val)/(2*a)),2)
if m <= sqrt1 <= n:
    print(sqrt1,list(range(m,n)))
if m <= sqrt2 <= n:
    print(sqrt2,list(range(m,n)))