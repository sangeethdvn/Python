# find the sum of squaree of n natural numbers

# n is entered by the user

n = int(input("Enter the number: "))

sum = 0

for i in range(1, n+1):

    i = i ** 2
    
    sum += i           #sum = sum + i ** 2

print(sum)