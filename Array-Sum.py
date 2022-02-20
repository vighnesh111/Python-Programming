#Python Program to find sum of array
array = []
sum = 0
n = int(input("Enter Number of Elements: "))
for i in range(0,n):
    elem = int(input())
    array.append(elem)
print(array)
for j in range(0,n):
    sum = sum + array[j]
print("Addition is", sum)
