import re

# txt = "Hello Python"

# pattern = "python"                      #o/p ==>  "No Match Found" since match is used[match is used at thr beginning only] 

# if re.match(pattern, txt):

#     print("Match Found")

# else:
    
#     print("No Match Found")


# =================================================================================================


# txt = "Python is a program"

# pattern = "program"  

# print("found" if re.search(pattern, txt) else "Not found")

# =================================================================================================

# txt = "Python is a program"

# pattern = "program"  

# result = re.search(pattern, txt)

# if result:

#     print(result.group())   # o/p ==> program

#     print(result.start())   # o/p ==> 12 [index of the 'P' in program]

#     print(result.end())     # o/p ==> 19 [index of after the 'm' in program]
    
# =================================================================================================

# txt = "python is  a programming library and python rules"

# patt = "python"


# match = re.findall(patt, txt)

# print(match)

# =================================================================================================

txt = "python is  a programming library and python rules"

patt = "python"


match = re.finditer(patt, txt)

for i in match:

    print(i.start())

    print(i.end())

    print(i.group())