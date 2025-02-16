# wap to check if there is a duplicate elements in the string

text = "welcome"

i = 0

a= " "

while i < len(text):

    if text.count(text[i]) > 1 and text[i] not in a:
        
        print(text[i])

        a = a + text[i]
    
    i += 1

