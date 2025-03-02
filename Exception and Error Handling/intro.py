# <<<<<<<<<< EXCEPTION  AND ERROR HANDLING >>>>>>>>>


"""
Handles errors that occur during the execution of a program
allows to respond to the error, instead of just crashing the program
it enables you to catch and manage errors, making your code more robust and more userfriendly

"""

"""
# DIVISION

a = int(input("Enter a number"))

b = int(input("Enter another number"))

result = a/b

print(result)   # will have error when b is 0 since you cant divide by zero

"""


# a = int(input("Enter a number"))

# b = int(input("Enter another number"))

# try:
    
#     result = a/b
#     print(result)

# except:

#     print("Error by division by zero")

# =================================================================================================



try:
    

    a = int(input("Enter a number"))

    b = int(input("Enter another number"))
    
    result = a/b
    
    print(result)

except ZeroDivisionError:

    print("Error by division by zero")

except ValueError:

    print("ENter a valid number")