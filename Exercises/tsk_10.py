"""

Write a function  that calculates the greatest common divisor (GCD) of two numbers a and b.

# """
def gcd(a,b):

    alist =[]

    blist = []

    combined_list =[]

    for i in range(1,a+1):

        if a % i == 0:

            alist.append(i)


    for i in range(1,b+1):

        if b % i == 0:

           blist.append(i)

    if len(alist) > len(blist):

        for i in alist :

            if i in blist :

                combined_list.append(i)

    else:

        for i in blist :

            if i in alist :

                combined_list.append(i)


    return(max(combined_list))


n1 = int(input("Enter first number: "))

n2 = int(input("Enter second number: "))

print("The GCD is: ",gcd(n1,n2))