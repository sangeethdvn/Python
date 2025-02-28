items = [1,2,2,3,3,3,4,4,4,4,5]

# o/p => {1:1,2:2,3:3,4:4,5:1}

result = {}

for i in items:

    result[i] = items.count(i)

print(result)
