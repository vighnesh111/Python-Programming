#Python Program for factorial of a number
num1 = int(input("Enter number:"))
fact = 1
if num1 == 0:
    print("Factorial is: 1")
elif num1 < 0:
    print("Enter a positive number")
else:
    while num1 != 1:
        temp = num1 
        num1 = (num1-1)
        fact = fact*temp
    print("Factorial is:", fact)



