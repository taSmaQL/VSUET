# 3.1.1
a = int(input("Введите первое целое число: ")) # 5 / 2
b = int(input("Введите второе целое число: ")) # 10 / 1
start = min(a, b)
end = max(a, b)

for i in range(start, end + 1):
    print(i, end=' ')
print("")


# 3.2.1
for i in range(start, end + 1):
    print(i)
    

# 3.2
p = int(input("Введите грузоподъемность грузовика в кг: "))

# print((a+b>p) ? "No, he can't" : "Yes, he can") it's not c++
print("No, he can't" if a + b > p else "Yes, he can")

