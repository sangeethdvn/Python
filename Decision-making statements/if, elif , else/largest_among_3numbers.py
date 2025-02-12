# wap to find largest among 3 numbers

a = int (input("Enter the number"))

b= int (input("enter the second number"))

c= int (input("enter the third number"))

if (a>b) and (a>c):
    
    print(f"{a} is largest of the three numbers")

elif (b>a) and (b>c):

    print(f"{b} is largest of the three numbers")

else:

    print(f"{c} is largest of the three numbers")