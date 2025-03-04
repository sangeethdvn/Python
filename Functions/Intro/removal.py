"""
Create a function to remove duplicate elements from the list

"""


def remove_duplicates(elements):

    new = []

    for i in elements:

        if i not in new:

            new.append(i)

    print(new)

remove_duplicates([1,2,3,2,3,4,5])