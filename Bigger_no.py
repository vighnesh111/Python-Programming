#Maximum of two numbers in Python
num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is smaller than", num2)
else:
    print("Both are equal")