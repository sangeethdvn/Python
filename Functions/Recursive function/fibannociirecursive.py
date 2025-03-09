def fibanocci(n):

    if n == 0:                          #}

        return n                        #}
                                                #} BAse CASE
    elif n == 1:                        #}

        return n                        #}
    
    elif n > 1:
                                                        #} recursive case
        return fibanocci(n - 1) + fibanocci(n - 2)
    
# print(fibanocci(5))

n = int(input("Enter the number: "))

for i in range (n):

    print(fibanocci(i))







