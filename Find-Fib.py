#Python Program for nth multiple of a number in Fibonacci Series
# 0 1 1 2 3 5 8 13 21....
num = int(input("Enter number: "))
a=0
b=1
c=a+b
numcheck = num
while (c < numcheck):
    c=a+b
    a=b
    b=c
if c == numcheck:
    print("FIB Number")
else:
    print("No a FIB Number")


        