inputFootballTeam = input("Prompt your desire football team: ")
print(f"{inputFootballTeam} is a champion!")
numbersInFootballTeam = len(inputFootballTeam)
print(numbersInFootballTeam * "-")
print(inputFootballTeam)
print(numbersInFootballTeam * "-")
lowerFootballTeam = inputFootballTeam.lower()
symbolsInFT = len(lowerFootballTeam)
letter = "p"
if lowerFootballTeam in letter:
    print("True. There's a letter P")
else:
    print("False. There's no letter P")
letterTwo = "a"
print(f"Letter A in football team are/is {lowerFootballTeam.count('a')}")