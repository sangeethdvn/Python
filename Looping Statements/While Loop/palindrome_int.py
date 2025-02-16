"""
a number that remains same when the digit id reversed is called palindrome

for example 121, 1331 and 4554 are all considered palindrome


"""

num = int(input("Enter a number you think is palindrome: "))    #156

rev =0

temp = num #156

while (num > 0):                #15

    digit = num % 10 #6      5

    rev = rev * 10 + digit #0 * 10+6 > 6 =>  6*10+5

    num = num // 10  #156 //10 > 15.6 > 15

if rev == temp:

    print(f"The given number {temp} is palindrome ")

else:

    print(f"The given number {temp} is not palindrome ")