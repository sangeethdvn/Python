items = {"a" :1, "b" :2, "c" :3}  #{1:"a", 2:"b", 3:"c"}

result ={}

for i in items:

    result[items[i]] = i  #result[1] = "a" #result[2] = "b" #result[3]= "c" 

print(result)