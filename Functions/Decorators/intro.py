# Decorators

# functions that modify the behavior of other functions, classes or methods
# without modifying its structure




def swap_number(fn):

    def wrapper(m1,m2):

        if m2 == 0 :

            m1,m2 =m2,m1

        return fn(m1,m2)
    
    return wrapper


@swap_number
def div(a,b):

    print(a/b)


div(4,0)