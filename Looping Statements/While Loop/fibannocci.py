# wap to print fibannocci 

# 0 1 1 2  3 5

num = int(input("Enter a number: "))

i = 2

a = 0

b = 1

print(a)

print(b)

while i <= num:

    c = a + b

    print(c)

    (a, b) = (b, c) #swapping

    i += 1