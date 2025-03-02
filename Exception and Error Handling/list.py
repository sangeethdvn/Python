#  wap to enter  a list of numbers

# 1>    try 

# 2> try to pick elements from a specific index  | indexerror|




#================================================================================================

numbers = [1, 2, 3, 4, 5]

try:

    index = int(input("Enter an index number: "))

    print(numbers[index])

except IndexError:
    
    print("Index is out of range....")

except ValueError:

    print("enter the correctvalue.....")











