"""

Write a function that returns a list of all divisors of n.

"""

def devisor(n):

    temp_list = []

    for i in range(1,n+1):

        if n % i == 0:

            temp_list.append(i)

    return(temp_list)

try:

    div = int(input("enter the number: "))

    if div == 0:

        print("Please enter number other than 0")

    elif div > 0:

        print(devisor(div))

except ValueError:

    print("Please enter integer only")