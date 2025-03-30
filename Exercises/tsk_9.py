""" 
Write a function  that takes an integer n and returns its reverse.
Example: reverse_integer(1234) should return 4321. 

"""

def reverse(r):

    r = str(r)

    return int(r[::-1])

n = int(input("Enter a number to be reversed: "))

print("Reversed Number: ", reverse(n))