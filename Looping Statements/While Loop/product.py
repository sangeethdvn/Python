#  wap tp write prodect of odd numbers from 1 to 10

i = 1

pro = 1

while i < 10:

    if i %  2 != 0:

        print(i)
        
        pro *= i
    
    i += 1

print(f"Product of odd numbers from 1 to 10: {pro}")