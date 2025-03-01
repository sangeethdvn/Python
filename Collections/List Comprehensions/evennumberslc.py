number =[1,2,3,4,5,6,7,8,9,10]

#  even =[]

# for i in numbers:

    # if i % 2 == 0:

        # even.append(i)

# print(even)

#  CAN BE SHORTENED TO SINGLE CODE BY LIST COMPRESHENSION

result = [i for i in number if i % 2 == 0]

print(result)