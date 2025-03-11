
numbers = [1,2,3,4,5,6,7,]

def square(a):

    return a ** 2

print([square(i) for i in numbers])

# /================================================================================================

print(list(map(lambda a: a**2 , numbers)))

# map (args1{function}, args2{list})

# The map()function is used to apply a given function to every item of a list or tuple

# list is manditory beacuse or else it will return answer in hexadecimal



