# 1
info = {}
info["fullName"] = {"Popov Kirill Trumpovich"}
info["date"] = {"10.10.2010"}
info["place"] = {"Severodvinsk"}
info["hobby"] = {"Gooning",'Jogging','Reading','Programming'}
info["animal"] = {"dogBellya","catVasya","wolfDaniel"}
info["USE"] = {} 
info["USE"].update({"Math":"95","Physics":"100","English":"100"})
info["USE"].update({"Chemistry":"20"})
del info["USE"]["Chemistry"]
info["Uni"] = {}
info["Uni"].update({"VSUET":"210","VSU":"55","VSTU":"10"})
# 2
print(f"Data: {info}")
exams = ["info","math","chemistry"]
print("Subjects:",exams)
uni = ["VSU","VSTU","VSUET"]
print("Uni:",uni)
# 3
name = "Kirill"
theVowels = ('a','e','i','o','u','A','E','I','O','U')
startsWithVowel = name.startswith(theVowels)
print("My name starts with vowel:",startsWithVowel)
month = 10
summer = [6, 7, 8]
autumn = [9, 10, 11]
spring = [3, 4, 5]
winter = [12, 1, 2]

def checkMonths(month):
    if month in summer:
        print("My birthday is in Summer.")
    elif month in autumn:
        print("My birthday is in Autumn.")
    elif month in spring:
        print("My birthday is in Spring.")
    elif month in winter:
        print("My birthday is in Winter.")
    else:
        print("Invalid month.")

checkMonths(month)
    
