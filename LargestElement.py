#Python Program to find largest element in an array
array = []
n = int(input("Enter Number of Elements: "))
for i in range(0,n):
    elem = int(input())
    array.append(elem)
print(array)
max = array[0]
for j in range(1,n):
    if array[j] > max:
        max = array[j]
print("Maximum is:", max)








