copnum = 50

g = int(input("enter a guess for the number: "))

if g != 50:

    if (copnum > g):

        if (copnum - g) >= 40 and (copnum - g) < 50:

            print('Too low')

        elif (copnum - g) >= 30 and (copnum - g) < 40:

            print("Not that low")

        elif (copnum - g) >= 20 and (copnum - g) < 30:

             print("Getting close!")

        elif (copnum - g) >= 10 and (copnum - g) < 20:

            print("very close")

        elif (copnum - g) < 10 :

            print("very very close")

    else : 

        if 40 <= (g - copnum) and (g - copnum) < 50:
                
                 print("Too high")
        
        elif  30 <= (g - copnum) and (g - copnum) < 40:
        
                print("Not that high")
        
        elif 20 <= (g - copnum) and (g - copnum) < 30:
        
                print("Getting close!")
        
        elif 10 <= (g - copnum) and (g - copnum) < 20:
        
                print("Very close")
        
        elif (g - copnum) < 10:
        
                print("Very very close")

else :

    print("You guessed it right Hurrah!!")