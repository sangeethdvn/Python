"""
The number 28 is a perfect number because its proper divisors sum up to give 28, and that is the definition of a perfect number.
 The divisors of 28 are 1, 2, 4, 7, 14, and 28. Therefore, the proper divisors of 28 are 1, 2, 4, 7, and 14.

"""

def pnum(a):

    sum = 0
    
    i = 1

    while i < a:

        if a % i == 0:

            print(i)

            sum += i

        i += 1

    if sum == a:

        print(f"{a} is a perfect number")

    else:

        print(f"{a} is not a perfect number")

pnum(28)