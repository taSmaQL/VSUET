a = int(input("Введите первое целое число: ")) # 5
b = int(input("Введите второе целое число: ")) # 500
c = int(input("Введите третье целое число: ")) # 3
listOfNumbers = [0,5,10,20,31,57,72,89,123,200,300,576,1023,2021,3124]
newList = []
for i in listOfNumbers:
    if (i > a) and (i < b) and (i % c == 0):
        newList.append(i)

print(newList)