def longest(txt):

    longest = 0

    for i in txt.split():

        if len(i) > longest:
        
            longest = len(i)

            new =  i

    print(new)

    print(longest)

longest("python is a progremming language")



    
