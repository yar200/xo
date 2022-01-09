import random
lst = [lst.random(90)]
maxNum = lst[0]

for num in lst:
    if num > maxNum:
        maxNum = num
print(maxNum)




import random

myList = []

for i in range(101):
    myList.append(random.randint(99, 100))