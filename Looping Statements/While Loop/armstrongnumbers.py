"""
number = 153

1**3 + 5**3 +3**3 =153

"""
# a positive integer that is equal to the sum of its digits, each raised to the power of the number of digits: 
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153



number = int(input("Enter a number: "))

temp = number

sum = 0

length = len(str(number))

while number > 0:

    digit = number % 10

    sum += (digit ** length)

    number = number // 10

if temp == sum:

    print(f"The given number is {temp} is Armstrong")

else:

    print(f"The given number is {temp} is not Armstrong")