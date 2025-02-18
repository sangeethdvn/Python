# wap to print even numbers upto n

n = int(input("enter a num: "))

for i in range(1, n+1):

    if i % 2 == 0:

        print(f"{i}")