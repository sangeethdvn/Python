# if the cost of the bikes is > 100000 and 15% TAX

# if the cost of the bike is > 50k and < 1L(both iclusive ) add 10% tax

# if cost <50k tax is 7%

amount = int(input("enter the amount: "))

if amount > 100000:

    tax = (amount * (15/100))

    print ("The tax to be included amount: ", tax)

    print ("total amount: ", amount + tax)

elif amount >= 50000 and amount <= 100000:

    tax= (amount * (10/100))

    print ("The tax to be included amount: ", tax)

    print ("total amount: ", amount + tax)

else:

    tax= (amount * (7/100))

    print ("The tax to be included amount: ", tax)

    print ("total amount: ", amount + tax)
