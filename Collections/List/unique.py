numbers = [1,8,3,7,5,10,1,4,3]  # o/p ==> [1,3,4,5,7,8,10]

unique = []

for i in numbers:

    if i not in unique:

        unique.append(i)

unique.sort()

print(unique)