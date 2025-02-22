# wap to print most recursive element in the list

elements = [1,4,2,2,3,5,1,3,2,6,7,2]

count =0

for i in elements:

    if elements.count(i) > count:

        count = elements.count(i)

        new = i
    
print(f" the elment is {i} and count is {count}")
