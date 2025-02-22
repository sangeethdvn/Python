numbers = [97,88,4,3,7,12,45,81,25]

smallest = numbers[0]

second_smallest = numbers[1]

for i in numbers:

    if i < smallest :

        second_smallest = smallest

        smallest = i

    elif i < second_smallest and i > smallest:

        second_smallest = i

print(f"{second_smallest} is the second smallest number.")