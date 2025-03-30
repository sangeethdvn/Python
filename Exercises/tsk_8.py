"""

Write a function  that takes a positive integer n and returns the sum of its digits

"""

def sumofdigits(temp):
    
    s = 0

    for i in  str(temp):

        s += int(i)

    return s

try:

    n = int(input("Entr a number: "))

    if n < 0:

        print("Positive Numbers Only")

    else:

        print(sumofdigits(n))

except ValueError:

    print("Invalid input")