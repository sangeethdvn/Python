"""

create a function to check  entered character is vowel or consonants

"""

def voworcon(x):

    return("Vowel" if x in "aeiouAEIOU" else "Consanents")

char = input("Enter character: ")

print(voworcon(char))


