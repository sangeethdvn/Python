items = {"a": 1, "b": 2, "c": 1, "d": 3, "e":2}

# removes both keys and values with same values 
result =[]

for i in items.copy():

    if items[i] in result:

        items.pop(i)

    elif items[i] not in result:

        result.append(items[i])

print(items)