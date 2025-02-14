course = "GVJVJHVJ"

print(course.capitalize())     #To capitalize first alphabet ina string     

print(course.upper())               #it is used to capitalize the entire string

print(course.lower())              #it is used to convert capitalization to lower case

print(course[-3])       #  acceess elemnts of a sequence from the end , using negative numbers as indexes

print(course.find("t"))  #  it is used to find the index of the element from the string

print(course.index("H"))    #   returns the index of the element in its forst occurence

print (course.isalpha())   # returns true or false checking if its alpabets or not

print (course.isalnum())   # returns true or false checking if its alpabets or not

print (course.isdigit())   # returns true or false checking if its numbers or not

print (course.isupper())   # returns true or false checking if its capitalaized or not

print (course.split("V")) # to split a string by given in/pu and return the splited o/p where the given element is ommited

print (course.find("v")) # to return index of a character

print (course.replace("v", "j")) # used to replace a character and  then replace with another character

print (course.strip("g")) # The strip() method removes any leading, and trailing whitespaces.

                                # Leading means at the beginning of the string, trailing means at the end.

                                # You can specify which character(s) to remove, if not, any whitespaces will be removed