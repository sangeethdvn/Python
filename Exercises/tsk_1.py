"""
    Given a pattern
    Text=”ABABC”
    Write a program to print first non-recursive character output=c without using nested loop
    
"""

txt = "ABABC"

for i in txt:

    if txt.count(i) == 1:       #outputs the first non-recursive character

        print(i)
