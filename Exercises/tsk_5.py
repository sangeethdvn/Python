"""
wap to print sum of even and odd indexed digits in a given number

"""

num  = int(input("Enter the number with some digits: "))

num = str(num)

sum_of_even = 0

sum_of_odd = 0

for i in num:

    if num.index(i) % 2 == 0:

        sum_of_even += int(i)

    else:

        sum_of_odd += int(i)

print(f"sum of even indexed digits ==> {sum_of_even} and odd indexed digits ==> {sum_of_odd}")