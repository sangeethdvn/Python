#entr a number by user

# check whether number is divisible by both 2 and 3 print "divisible by both"  eg : 6

# check number divisible only by 2 and not by 3 >> divisible by only2  eg: 4

# check number  divisble by either 2 or 3 >>(either 2 or 3) # 68

# check number not divisible by both 2 and 3 >>(not divisible by both) # 5

num = int(input("enter the number"))

if num % 2 == 0 and num % 3 == 0:

    print (f"{num} Number is divisible by both 2 and 3")

elif num % 2 == 0 and num % 3 != 0:

    print (f"{num} Number is divisible by 2 not 3")

elif num % 2 == 0 or num % 3 == 0:

    print (f"{num} Number is divisible by 2 or 3" )

elif num % 2 != 0 and num % 3 != 0:   

    print(f"{num} is not divisible by both 2 and 3")


    