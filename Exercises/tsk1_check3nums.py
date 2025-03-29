a = int(input("Enter the first number: "))

b = int(input("Enter the second number: "))

c = int(input("Enter the third number: "))

#  a > b  and a > c
# compare between b and c
# B > C ==> ?? SECOND LARGEST NUMBER

if a > b and a > c:

    if b > c:

        print (f"{b} is the second largest number ")

    else:
        
         print (f" {c} is the second largest number ")

elif b > c and b > a:

    if c > a:

        print(f" {c} is the second largest number ")

    else:

        print(f"{a} is the second   largest number ")

elif c > a and c > b:

    if a > b:

        print(f" {a} is the second  largest number ")
    
    else:
        
        print(f" {b} is the second largest number ")