"""
wap to print the characters of a string in even positions. >>>      txt= "python"    o/p = y h n

"""


txt = "python"

for i in txt:

    if txt.index(i) %2 != 0:

        print(i, end=" ")
