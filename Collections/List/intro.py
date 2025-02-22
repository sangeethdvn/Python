"""
List : collection , python used to assign more than one element to a variable

lists are used to store more than one value to a variable
                                                                                                                # ORDERED
we can store all types of datatypes in a variable                                                               # CHANGABLE
                                                                                                                # ALLOW DUPLICATES        


"""

# LISTS
# ================================================================

# items = []  ==> SYntax

# It is also possible to use the list() constructor when creating a new list.

#       thislist = list(("apple", "banana", "cherry"))
            # print(thislist)                               o/p ==> ['apple', 'banana', 'cherry]

# ================================================================

# items = [1,2,3,4,5,6,7,8,9]

# items[2] ==> "3"

# ================================================================


# print(type(items))     <class 'str'>

# items = [1,2,3,4,5,6,7,8,9]

# items = [1,"hajks","nsjk",2,False]  ========> Heterogeneous

                # items = [1, 2,"hello",True,2,1]

                # print(len(items))

# ================================================================


# METHOS IN LISTS

# ================================================================

items = [1,2,3,4,5,6,7,8]

items.append("HARI") #==> add an element to the last pposition of the list

items.insert(2,True) #==> to add an element to the specified index position and the value of the specified position is moved to the next position
                                        # items.insert(index pos of value to be added, Value)


items.pop() # ==> if no values is given in method ie indes position it will remove last element and print the same element value
                    #if position is given it will remive the value in the position and print the value in the same position
                    

items.count() #==> it is used to count the number of occurrences given inside the bracket[value]    

items.sort() #==> it is used to sort the values u=in ascending order

items.sort(reverse=True)  #==> to get the list values in descending order

items.remove("hI") #==> remove  the first occurence of the value

items.clear() #==> cleaall the elements and still show as an empty list

items.extend(10,11,12) #==> add a new list of elements as a continuation of the previous list

items.index(5) #== (value) o/p the index postion of the value if there are duplicates it will o/p the the position of the first value

