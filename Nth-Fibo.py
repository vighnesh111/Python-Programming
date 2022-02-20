# Python Program for n-th Fibonacci number
# 0 1 1 2 3 5 8 13 21....
nth = int(input("Enter number: "))
if nth == 1:
    print(0)
elif nth == 2:
    print(0)
    print(1)
elif nth >=3:
    m = 0
    n = 1
    print(0)
    print(1)
    for i in range(2, nth):
        block = m+n
        m = n
        n = block
        print(block)
