# wap to find devisors of a number

num = int(input("Enter a number: "))

i = 1

while i < num:

    if num  % i == 0:

        print(i)

    i += 1