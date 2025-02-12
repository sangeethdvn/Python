# wap to check wether its odd or even

a = int(input("Enter a number: "))

b = int(input("Enter second number: "))

if (a % 2 == 0 ) and (b % 2 == 0):
    print(f"the given number {a}  and {b} are even")

else:

    print(f"the given number {a} or  {b} is odd")