# *args allow you to pass multiple arguments  to a function

def addition(*a):    #ARGS are stored in a TUPLE

    sum = 0

    for i in a:

        sum += i

    print(sum)


addition(56,23,5612,23)

addition(5,2,5,2,8,7,8,6)