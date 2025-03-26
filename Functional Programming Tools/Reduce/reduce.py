from functools import reduce

num =[1,2,3,4]

print(reduce(lambda a,b: a + b,num))