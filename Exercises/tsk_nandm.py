n = int(input("Enter the Beginning of the number: "))

m = int(input("Enter the Last number: "))


# num= list(range(n,m+1))

# print(f"List of numbers: {num}")        

numbers = []

for i in range(n,m+1):

    numbers.append(i)

print(numbers)