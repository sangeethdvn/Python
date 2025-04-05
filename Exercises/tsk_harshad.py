# 27 is a harshad number , as the sum of the digits is 27 is 9 and the number is divisible by 9

def harshad(a):

    temp = a 

    sum = 0
     
    while a > 0:
        
        dig = a % 10

        a = a // 10

        sum += dig

    # if temp % sum == 0:

    #     print("Harshad Number")

    # else:

    #     print("Harshad number NOT!!!")


    print("Harshad Number" if temp % sum == 0 else "Harshad number NOT!!!")

harshad(27)
