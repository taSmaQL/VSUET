firstTuple = ("hello", "world","my", "name", "is", "skibidi", "toilet","my", "name", "is", "skibidi", "toilet",)
emptyTuple = tuple()
element = input()
if element in firstTuple:
    if firstTuple.count(element) == 1:
        firstIndex = firstTuple.index(element)
        newTuple = firstTuple[firstIndex:]
        print(newTuple)
    elif firstTuple.count(element) > 1:
        index = firstTuple.index(element)
        firstIndex = firstTuple.index(element)
        secondIndex = firstTuple.index(element, firstIndex + 1)
        newTuple = firstTuple[firstIndex:secondIndex + 1]
        print(newTuple)
else:
    print(emptyTuple)


