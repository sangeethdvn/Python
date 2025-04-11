numbers =[6,23,51,18]

perfect = []

for i in numbers:

    sum = 0

    for j in range(1,i):

        if i % j == 0:

            sum += j
        
    if sum == i:

        perfect.append(i)

print(perfect)