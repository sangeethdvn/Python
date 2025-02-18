    # Python is a programming language

# wap to find largest word in a string

text = "Python is a programming language"

largest = 0

for i in text.split(" "):

    if (len(i) > largest):

        largest = len(i)

        element = i

print (largest)

print(element)