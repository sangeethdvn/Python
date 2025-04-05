def devisors(num):

    for i in range(1,num+1):

        if i <= num and num % i == 0:

            print(i)

devisors(27)