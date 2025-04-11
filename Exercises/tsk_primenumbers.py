numbers = [2, 4, 7, 9, 11, 14, 17, 20, 23, 25]

prime =[]

for i  in numbers:  

    for j in range(2,i): #2,3,4,5 <num because the only value privme should be divided is 1 and num itself

        if i % j == 0:

            break

    else:

            prime.append(i)

print(prime)

        


