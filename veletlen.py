import random

print("_________________________________________________________")

numberList = []

for i in range(0,10):
    n = random.randint(1,20)
    numberList.append(n)

a=sum(numberList)/len(numberList)



print("A random számok: "+str(numberList))
print(" ")
print("A számok átlaga: "+str(a))
print(" ")
print("A legkisebb random szám: "+str(min(numberList)))
print(" ")
print("A legnagyobb random szám: "+str(max(numberList)))
print(" ")

if (9 in numberList):
    print("Van benne 9")

print("_________________________________________________________")
