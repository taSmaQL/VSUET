numberTempleWithoutFloat = (1,9,100,49,81,25)
# print(sorted(numberTempleWithoutFloat))
numberTempleWithFloat = (1,9,100,3.2,49,52.4)
# for index,item in enumerate(numberTempleWithFloat):
    # if type(item) == float:
    #     print('There is a float in temple')
    #     print(numberTempleWithFloat)
    #     break
    # elif 
    #     print(index, sorted(numberTempleWithFloat))
def checkFloat(tuple1):
    for index,item in enumerate(tuple1):
        if type(item) == float:
            return True
    return False

if checkFloat(numberTempleWithoutFloat):
    print(numberTempleWithoutFloat)
else:
    print(sorted(numberTempleWithoutFloat))
if checkFloat(numberTempleWithFloat):
    print(numberTempleWithFloat)
else:
    print(sorted(numberTempleWithFloat))
