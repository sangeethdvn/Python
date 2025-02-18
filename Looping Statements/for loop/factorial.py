n = int(input("Enter thr number for factorial: "))

fact =1

for i in range(1,n+1):

    fact = i * fact

print(f"factorial of {n} is {fact}")