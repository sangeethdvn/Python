#  o/p => yhn

text = "python"

result = ""
for i in text:

        if(text.index(i) % 2 != 0):
                print(i, end ="")
                result = result + i

print(result)

