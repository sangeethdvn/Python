mobiles={"Apple":{"model":"iphone15","price":120000,"color":"Black"},
         "Samsung":{"model":"S23 Ultra","price":180000,"color":"white"},
         "Sony":{"model":"xperia ultra","price":130000,"color":"red"},
         "Huawei":{"model":"Pura 70 ultra","price":170000,"color":"Black"}
         }

"""

prive above 50k

iphone or  xperia

colors other than black

Black in color whose price is less than 150000

ultra in model name


"""

# print(mobiles["Apple"]["model"])

for i in mobiles:
#    print(mobiles[i])    #values of i {which are apple, smasung that are keys i}

# ================================================================\ 
   
    # if mobiles[i]["color"] == "Black":

    #     print(i)

# =================================================================\

    # if mobiles[i]["price"] > 50000:

    #     print(i)

# =================================================================\

    # if mobiles[i]["color"] != "Black":

    #     print(i)

# =================================================================\

    # if mobiles[i]["color"] == "Black" and mobiles[i]["price"] < 150000:

    #         print(i)

# ==================================================================\

    # if  100000 < mobiles[i]["price"] < 150000:

    #     print(mobiles[i]["model"])

# ==================================================================\

    if  100000 < mobiles[i]["price"] < 150000 and mobiles[i]["color"] == "red":

        print(mobiles[i]["model"])
