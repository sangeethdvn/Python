# wap to find the largest string without repeating alphabets

text = "python is a programming language"

# text = text.split("")
largest = ""

for i in text.split(" "):

    for j in i: #p 

        if i.count(j) > 1:

            break

    else:

        if len(i) > len(largest):

            largest = i

print(largest) 

