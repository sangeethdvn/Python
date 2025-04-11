#smallest evn num ina list

num =[88,22,99,47,33,84,85]

num.sort()

print(num)

for i in num:
    
    if (i % 2 ==0):
    
        print("smallest even in list:",i)
        
        break