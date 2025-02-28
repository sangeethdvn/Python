text = "programming"

# o/p ==>{"p":1,"r":2,"o":1,"g":2,"a":1,"m":2,"i":1,"n":1}

result ={}

for i in text:

    result[i] =  text.count(i)

print(result)


"""
new = ""/
for i in text:

    count =1

    if i in new :
    
        count += 1
    
    new += i

    print(i, count)

"""