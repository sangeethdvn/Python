# 27 is a harshad number , as the sum of the digits is 27 is 9 and the number is divisible by 9

num = int(input("Enter a number: "))

sum = 0

for i in str(num):

    sum += int(i) 

print(sum)

if num % sum == 0:

    print("Number is harshad number")
        
else:

    print("Number is not harshad number")

