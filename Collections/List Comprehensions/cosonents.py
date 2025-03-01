txt = "pythonlanguage"

# for i in txt:

#     if i not  in "aeiou":

#         print(i)


result = [i for i in txt if i not in "aeiou"]

print(result)

unique= []

for i in result:

    if i not in unique:

        unique.append(i)

print(unique)