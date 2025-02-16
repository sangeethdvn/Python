"""
The number 28 is a perfect number because its proper divisors sum up to give 28, and that is the definition of a perfect number.
 The divisors of 28 are 1, 2, 4, 7, 14, and 28. Therefore, the proper divisors of 28 are 1, 2, 4, 7, and 14.

"""


number = int(input("enter the number: "))

i= 1

sum =0

while (i < number):

    if number % i == 0:

         print(i)

         sum += i    
    
    i += 1

if sum == number:
     
     print(f"{number} is a perfect number")

else:
     
     print(f"{number} is not a perfect number")