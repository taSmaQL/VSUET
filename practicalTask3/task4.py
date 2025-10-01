stringSt = "Pick up a uni is pretty ambiguous choice. It is very hard to chose where you need to start your first career".lower()
stringSubst = "ambiguous".lower()
stringFalse = "small".lower()
listStringFirst = stringSt.split()
if stringFalse in listStringFirst:
    print(f"Correct. There's {stringFalse} in '{stringSt}'")
if stringSubst in listStringFirst:
    print(f"Correct. There's {stringSubst} in '{stringSt}'")
'''
ChatGPTу не нравится моё решение, то есть оно говорит, что моё решение не корректно. Я с ним согласен, 
но и одновременно нет. Может я пока не додумался почему я не прав.

Ответ ChatGPT:
    В задаче же от тебя хотят проверить именно наличие подстроки в строке (не важно, слово это или часть слова).

    Правильнее было бы без .split() — вот так:

    stringSt = "Pick up a uni is pretty ambiguous choice. It is very hard to chose where you need to start your first career".lower()
    stringSubst = "ambiguous".lower()
    stringFalse = "small".lower()

    if stringFalse in stringSt:
        print(f"Подстрока есть: {stringFalse}")
    else:
        print("Подстроки нет")

    if stringSubst in stringSt:
        print(f"Подстрока есть: {stringSubst}")
    else:
        print("Подстроки нет")
'''