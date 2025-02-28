text = "python is good programming language"

# {"Python" : 6 ,................................,"language":8}

result = {}

for i in text.split():

    result[i] = len(i)  #means a=> result[python] = 6 =>{"python" : 6}
    
print(result)