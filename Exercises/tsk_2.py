"""
    Given a pattern text=”ABEABAIACB”
   Write a program to print most recursive consonant from above text 
   Output=B
"""
txt = "ABEABAIACB"

temp = ""

another_temp = ""

for i in txt:

    if txt.count(i) > 1 and i not in "aeiouAEIOU":

        temp += i

for i in temp:

    if i not in another_temp :

        another_temp += i

print(another_temp)

