num = [1,2,3,4,5]

def square(a):

    return (a**2)

new = []

for i in num:

   print(square(i))

   new.append(square(i))

print(new)

