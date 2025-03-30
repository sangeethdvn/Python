"""

wap to find the prime numbers below n where n is entered by user


"""

n = int(input("Enter the number upto where you want the prime number sequence: "))

li = []

for i in range(2,n+1):

    for j in range(2,n+1):

        if i % j == 0:

            break

        else:

            li.append(i)

            break

print(li)
