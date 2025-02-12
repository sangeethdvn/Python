"""
if the numbe is under 10 => "too low"
number between 10 and 20 is(inclusive) => "CorreECT"
otherwise display => "Too high

"""


num = int (input("Enter a number to be checked: "))

# if num < 10:

#     print("two low")

# elif num >= 10 and num <= 20:

#     print("Correct")

# else:
    
#     print("Too high")

print("two low " if num < 10 else "Correct" if 10 <= num <= 20 else "Too high")


