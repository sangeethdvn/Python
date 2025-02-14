text = "python"   #npytho

result =  text[-1] + text[0::]

print(result)

# =================================================================

txt = "hellopython"     #ollehpython

if "p" in txt:

    item = txt[0:txt.index("p")]

    print(item) 

#               print(item[::-1]) ==> olleh (to reverse a string)

    # print(item[::-1] + txt[txt.index("p")::])

    # print(olleh + txt[5::])
    # print(olleh + python)
    # ollehpthon
# else:

    # print("thank you")