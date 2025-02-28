txt ="every moring is a fresh begininng"

wrd_ct ={}

words = txt.split(" ")

for i in words:

    asci = 0 

    for j in i:

        asci += ord(j)

    wrd_ct[i] = asci

print(wrd_ct)

max = 0

for i in wrd_ct:

    if wrd_ct[i] > max:

        max = wrd_ct[i]

        element = i
    
print(element, max)
