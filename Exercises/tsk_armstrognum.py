# a positive integer that is equal to the sum of its digits, each raised to the power of the number of digits: 
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153


def armnum(a):

    length = len(str(a))

    sum = 0

    temp = a

    while a> 0:

        dig = a % 10 

        sum += (dig ** length)

        a = a // 10

    print(f"{temp} = {sum}")

    if temp == sum:

        print(f"{temp} is armstrong number")

    else:

        print(f"{temp} is not armstrong number")

armnum(153)



# ================================================================================================================================
"""
def isarm(a):

    length = len(str(a))

    sum = 0

    for i in str(a):
    
        sum = sum + int(i)**length

    print("armstrong number" if sum == a else "Not armstrong number")


isarm(153) 
"""