#Python Program to check Armstrong Number
num = int(input("Enter the number to check: "))
temp = num
if num == 0 | 1 :
    print("Armstrong number")
elif num > 1000:
    print("Not an Armstrong Number")
else:
    if num < 1000:
        D1 = int(num/100)
        SUB = D1*100
        num = num-SUB
        if num < 100:
            D2 = int(num/10)
            SUB = D2*10
            num = num-SUB
            D3 = num
            dupnum = int(((D1**3)+(D2**3)+(D3**3)))
            if temp == dupnum:
                print("Armstrong Number")
            else:
                print("Not an Armstrong Number")
