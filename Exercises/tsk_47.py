a = int(input("Enter a number: "))

b = int(input("Enter another number: "))

sum = a + b

temp = 0

print(f"Sum of the above two numbers: {sum}")

qn = input("Do you wish to continue? (y/n): ")

while qn == "y" or qn == "Y": 

    temp = int(input("Enter the new number to be added: "))

    sum = sum + temp

    print(f"Updared sum: {sum}")

    qn = input("Do you wish to continue? (y/n): ")