fruit_p ={

    "apple" :0.52,
    "baanan" :45,
    "kiwi" :.19
}

for i in fruit_p.copy():  # to make a duplicate copy of fruit_p and process on it

    if i == "kiwi":

        fruit_p.pop(i)

        fruit_p["orange"] = 0.56

print(fruit_p)