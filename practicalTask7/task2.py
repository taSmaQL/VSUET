# 2.1
listOfNumbers = [100,84,68,51,23,19,3,0]
sum = 0
totally = 0
for i in listOfNumbers:
    sum += i
    totally += 1
print(sum)
print(totally)


# 2.2
listOfNumbers1 = [0,5,10,15,20,25] # Тут не понятно, продолжается ли список или остановливается до 25.
x = 20
for i in listOfNumbers1:
    if x > i:
        print(i)