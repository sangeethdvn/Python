# this user seems to be dumb

txt = "jkl has been wrt"

length = 0

for i in  txt.split(" "):

    for j in i:

        if j in "aeiou" :

            break
    
    else:

        print(i)





