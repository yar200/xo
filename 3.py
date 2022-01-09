import random
myList = []
for i in range(101):
    myList.append(random.randint(1, 5277575))
print(myList)

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]