items ={2:8, 4:6,7:9, 1:2}

# o/p ==> [10, 10, 16,3]

li =[]

for i in items:
    
    sum = 0
    
    sum = i + items[i]

    li.append(sum)

print(li)

# =================================================================

# print([i+ items[i] for i in items])
    