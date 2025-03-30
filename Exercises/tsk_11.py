"""

Write a function  that returns the sum of the first n natural numbers using the formula:
Sum = n(n+1)/2

"""

def sumofn(x):

    for i in range(x + 1):

        s = (x * (x + 1)) / 2

        return s
    
n = int(input("Enter the upto which natural numbers you want to sum: "))

print(sumofn(n))