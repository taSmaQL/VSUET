import math
m = 700
minInDay = 1440
n = math.floor(m/60)
p = (round(math.ceil(m/60) - m/60,2))
print(f"an integer number of hours elapsed since the beginning of the day is {n} hours and the number of minutes elapsed since the start of the last hour approximately {p} minutes")