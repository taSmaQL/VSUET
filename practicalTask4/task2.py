listOne = ['Wassup','My','Name','Is']
listTwo = ['I','Like','Pizza']
listThree = ['Okey']
finalLen = len(max(max(listOne),max(listTwo),max(listThree)))
for index,item in enumerate(listOne):
    if len(item) < finalLen:
        listOne[index] = item + "_" * (finalLen - len(item))
for index,item in enumerate(listTwo):
    if len(item) < finalLen:
        listTwo[index] = item + "_" * (finalLen - len(item))
for index,item in enumerate(listThree):
    if len(item) < finalLen:
        listThree[index] = item + "_" * (finalLen - len(item)) 

print(f"{listOne}\n{listTwo}\n{listThree}")