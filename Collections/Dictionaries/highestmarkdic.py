"""
Make a dictionary of student names and their scores.(5 element)

>> find the highest score
>> find the smallest score

sample dictionary format : {"arun":98,"a":78,"b":64}

arun , a,b

"""

details = {"a":77, "b":64, "c":56, "d":84, "e":45}

# largest = 0

# smallest = 0

# for i in details.values():

#     if i > largest :

#         largest = i

# print(largest)

# print(min(details.values()))

# =================================================================================================

largest = 0

smallest = 100

for i in details:

    smallest = min(smallest, details[i])    #details of i means the values 

    largest = max(largest, details[i])

print(largest)

print(smallest)

