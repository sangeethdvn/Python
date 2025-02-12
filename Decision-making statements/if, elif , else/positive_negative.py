# wap to check if a given number is positive or negative or zero

num = int(input("enter the number"))

if num > 0:

    print(f"{num} is positive")

elif num < 0:

    print(f"{num} is negative")

else:

    print(f"{num} is Zero")


print("+ve" if num>0 else "")