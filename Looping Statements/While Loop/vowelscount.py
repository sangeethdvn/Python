    #  wap to find the count of vowels in a string


text = "helloworld"

i =0

count = 0

while i < len(text):

    if text[i] in "aeiou":

        count = count + 1
    
    i += 1

print("the count", count)


# ================================================================

