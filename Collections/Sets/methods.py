

# ================================================================================================================================
# set1.add()    # add an element to the set
 
# set1.pop()          # reove a  random element from the set

# set1.remove()        # remove a specified element (argument) from the set

# set1.clear()        # clears out thr whole set

# ================================================================================================================================

# set1 ={1,2,3,4,5,6}

# set2 ={1,2,7,8,9,10}

# print(set1.union(set2))

# print(set1.intersection(set2))

# print(set1.difference(set2))    #in this the difference between set1 and set2 in taken which means that the value in set 1 are showed and not the values in set2

# print(set2.difference(set1))    ##in this the difference between set2 and set1 in taken which means that the value in set 2 are showed and not the values in set1

# ==================================================================================================================================


set1 = {1,2,3,4,5,}

set2 ={3,4,5}

# print(set1.issuperset(set2))  # return true if all elements of set 2 are in set 1. Then set 1 is superset and set2 is subset of set1

# print(set2.issubset(set1))  # return true if all elements of set 2 are in set 1. Then set 1+2 is subset of set1

# print(set1.issubset(set2))

# set1.discard(5)   # discard the elemnt in the arguement

print(set1.isdisjoint(set2)) #Return True if no items in set set1 is present in set2

set1.difference_update(set2) #remove all elements of set 2 that are in set 1

set1.intersection_update(set2) #o/ps the set 1 as the value in the both of them.