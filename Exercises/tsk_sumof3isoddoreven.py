def sum():

    sum = 0

    a = int(input("enter a number: "))  
    
    b = int(input("Enter another number: "))

    c = int(input("Enter the third number: "))

    sum = a + b + c

    if sum % 2 == 0:

        print(f"Sum of the three numbers is even: {sum}")

    else:

        print(f"Sum of the three numbers is odd: {sum}")

sum()        